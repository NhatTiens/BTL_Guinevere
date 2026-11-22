"""GUINEVERE - Game RPG gui Python thuần (Tkinter).

Phần giao diện đã hoàn thiện. Học viên chỉ chỉnh file logic.py.
Chạy: python main.py
"""

import tkinter as tk
from tkinter import messagebox
import logic

BG = "#0D1424"
PANEL = "#172237"
PANEL_LIGHT = "#202F49"
GOLD = "#F2C66D"
WHITE = "#F3F5FA"
MUTED = "#ADBCD3"
GREEN = "#79D7AC"
RED = "#F18D8D"
BORDER = "#33435F"
FONT = "Segoe UI"

MAX_SCENES = 9

SCENES = [
    {
        "title": "RỪNG SƯƠNG MÙ",
        "tag": "01 / GIAO TRANH",
        "description": "Một yêu tinh Goblin nhảy ra giữa đường, chặn lối vào khu rừng.\n"
                       "Ngươi sẽ chiến đấu để nhận vàng và kinh nghiệm, hay đi đường vòng?",
        "primary": ("CHIẾN ĐẤU", "goblin"),
        "secondary": ("ĐI ĐƯỜNG VÒNG", "skip"),
        "symbol": "⚔",
    },
    {
        "title": "SUỐI ÁNH TRĂNG",
        "tag": "02 / HỒI PHỤC",
        "description": "Một dòng suối trong vắt chảy giữa rừng.\n"
                       "Nếu uống nước suối, hiệp sĩ có thể hồi phục 20 HP.",
        "primary": ("UỐNG NƯỚC SUỐI", "heal"),
        "secondary": ("BỎ QUA", "skip"),
        "symbol": "✦",
    },
    {
        "title": "BỌN CƯỚP ĐƯỜNG",
        "tag": "03 / GIAO TRANH",
        "description": "Nhóm Bandit đòi thu phí để vượt qua chiếc cầu gỗ.\n"
                       "Bạn có thể giao chiến hoặc đi đường vòng.",
        "primary": ("ĐÁNH BỌN CƯỚP", "bandit"),
        "secondary": ("ĐI ĐƯỜNG VÒNG", "skip"),
        "symbol": "⚔",
    },
    {
        "title": "RƯƠNG KHO BÁU",
        "tag": "04 / PHẦN THƯỞNG",
        "description": "Giữa những tảng đá, bạn tìm thấy một chiếc rương cổ.\n"
                       "Mở rương sẽ nhận 20 Gold (tối đa 100 Gold).",
        "primary": ("MỞ RƯƠNG", "treasure"),
        "secondary": ("RỜI ĐI", "skip"),
        "symbol": "◆",
    },
    {
        "title": "CỬA HÀNG DU MỤC",
        "tag": "05 / MUA SẮM",
        "description": "Một thương nhân chào bán thuốc hồi phục Remedy.\n"
                       "Một bình thuốc có giá 15 Gold. Bạn mang tối đa 5 bình.",
        "primary": ("MUA REMEDY (15 G)", "buy"),
        "secondary": ("KHÔNG MUA", "skip"),
        "symbol": "✚",
    },
    {
        "title": "PHÙ THỦY MERLIN",
        "tag": "06 / PHÉP THUẬT",
        "description": "Merlin xuất hiện với một lời chúc phúc trước trận chiến lớn.\n"
                       "Nhận phép thuật để tăng 1 Level và hồi 10 HP.",
        "primary": ("NHẬN CHÚC PHÚC", "merlin"),
        "secondary": ("TỪ CHỐI", "skip"),
        "symbol": "✧",
    },
    {
        "title": "CỔNG ĐÁ TROLL",
        "tag": "07 / GIAO TRANH",
        "description": "Quỷ Troll trấn giữ lối vào lâu đài.\n"
                       "Nếu đủ sức mạnh, chiến thắng sẽ mang lại vàng và cấp độ mới.",
        "primary": ("CHIẾN ĐẤU", "troll"),
        "secondary": ("TRÁNH GIAO TRANH", "skip"),
        "symbol": "⚔",
    },
    {
        "title": "KHO DỰ TRỮ CỔ",
        "tag": "08 / VẬT PHẨM",
        "description": "Trong hầm ngầm, hiệp sĩ tìm được một PhoenixDown.\n"
                       "Vật phẩm này có thể hồi sinh tự động khi HP về 0 (tối đa 3).",
        "primary": ("NHẶT PHOENIXDOWN", "phoenix"),
        "secondary": ("BỎ QUA", "skip"),
        "symbol": "✦",
    },
    {
        "title": "BOWSER - TRÙM CUỐI",
        "tag": "09 / QUYẾT ĐẤU",
        "description": "Công chúa Guinevere đang bị nhốt phía sau ngai vàng!\n"
                       "Để đánh bại Bowser: Level ≥ 5 và HP ≥ 40.\n"
                       "Có thể dùng Remedy ở bảng điều khiển trước khi quyết đấu.",
        "primary": ("ĐỐI ĐẦU BOWSER", "bowser"),
        "secondary": ("RÚT LUI", "retreat"),
        "symbol": "♛",
    },
]


def new_hero():
    return {
        "hp": 100, "max_hp": 100, "level": 2,
        "gold": 15, "remedy": 1, "phoenix": 0,
    }


class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("GUINEVERE | Nhiệm vụ giải cứu công chúa")
        self.root.geometry("1110x735")
        self.root.minsize(980, 665)
        self.root.configure(bg=BG)
        self.hero = new_hero()
        self.scene = 0
        self.finished = False
        self.result = None
        self._build_ui()
        self.restart(first_time=True)

    def _label(self, parent, text, size=11, color=WHITE, bold=False, **kw):
        return tk.Label(
            parent, text=text, bg=parent.cget("bg"), fg=color,
            font=(FONT, size, "bold" if bold else "normal"), **kw,
        )

    def _button(self, parent, text, command, primary=False, danger=False):
        bg = GOLD if primary else ("#71404B" if danger else PANEL_LIGHT)
        fg = BG if primary else WHITE
        btn = tk.Button(
            parent, text=text, command=command,
            font=(FONT, 10, "bold"), bg=bg, fg=fg,
            activebackground="#F7D78F" if primary else BORDER,
            activeforeground=BG if primary else WHITE,
            relief="flat", bd=0, cursor="hand2",
            highlightthickness=0, padx=15, pady=12,
            disabledforeground="#8992A7",
        )
        return btn

    def _card(self, parent):
        return tk.Frame(parent, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)

    def _build_ui(self):
        header = tk.Frame(self.root, bg=BG, padx=30, pady=19)
        header.pack(fill="x")
        self._label(header, "GUINEVERE", 25, GOLD, True).pack(side="left")
        self._label(header, "  /  HÀNH TRÌNH GIẢI CỨU CÔNG CHÚA", 11, MUTED, True).pack(side="left", pady=(12, 0))
        self._button(header, "CHƠI LẠI", lambda: self.restart(), danger=False).pack(side="right")

        main = tk.Frame(self.root, bg=BG, padx=24)
        main.pack(fill="both", expand=True, pady=(3, 15))
        main.grid_columnconfigure(0, minsize=224, weight=2)
        main.grid_columnconfigure(1, minsize=390, weight=4)
        main.grid_columnconfigure(2, minsize=245, weight=3)
        main.grid_rowconfigure(0, weight=1)

        # Left: full hero status, always visible.
        sidebar = self._card(main)
        sidebar.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        left = tk.Frame(sidebar, bg=PANEL, padx=18, pady=19)
        left.pack(fill="both", expand=True)
        self._label(left, "HỒ SƠ HIỆP SĨ", 12, GOLD, True).pack(anchor="w")
        self._label(left, "Hiệp sĩ Bàn Tròn", 16, WHITE, True).pack(anchor="w", pady=(16, 3))
        self._label(left, "Sứ mệnh: giải cứu Guinevere", 10, MUTED).pack(anchor="w")
        tk.Frame(left, height=1, bg=BORDER).pack(fill="x", pady=17)
        self._label(left, "SỨC KHỎE (HP)", 10, MUTED, True).pack(anchor="w")
        self.hp_label = self._label(left, "100 / 100", 17, GREEN, True)
        self.hp_label.pack(anchor="w", pady=(5, 6))
        self.hp_bar = tk.Canvas(left, height=13, bd=0, bg=PANEL_LIGHT, highlightthickness=0)
        self.hp_bar.pack(fill="x")
        self.hp_bar.bind("<Configure>", lambda _: self.update_stats())
        self.values = {}
        for title, key in (("Cấp độ", "level"), ("Vàng", "gold"), ("Remedy", "remedy"), ("PhoenixDown", "phoenix")):
            line = tk.Frame(left, bg=PANEL, pady=10)
            line.pack(fill="x")
            self._label(line, title, 11, MUTED).pack(side="left")
            val = self._label(line, "—", 14, WHITE, True)
            val.pack(side="right")
            self.values[key] = val
        tk.Frame(left, height=1, bg=BORDER).pack(fill="x", pady=12)
        self._label(left, "TÚI ĐỒ", 11, GOLD, True).pack(anchor="w")
        self._label(left, "Remedy: hồi 40 HP.\nPhoenixDown: tự hồi sinh.", 10, MUTED, justify="left").pack(anchor="w", pady=(7, 13))
        self.potion_btn = self._button(left, "SỬ DỤNG REMEDY", self.use_potion)
        self.potion_btn.pack(fill="x", pady=2)

        # Centre: current event, always displays every relevant choice.
        centre = self._card(main)
        centre.grid(row=0, column=1, sticky="nsew", padx=5)
        content = tk.Frame(centre, bg=PANEL, padx=25, pady=22)
        content.pack(fill="both", expand=True)
        self.step_label = self._label(content, "SỰ KIỆN 01 / 09", 11, GOLD, True)
        self.step_label.pack(anchor="w")
        self.symbol = self._label(content, "⚔", 60, GOLD, True)
        self.symbol.pack(pady=(22, 4))
        self.tag = self._label(content, "01 / GIAO TRANH", 10, MUTED, True)
        self.tag.pack(pady=(0, 9))
        self.event_title = self._label(content, "RỪNG SƯƠNG MÙ", 20, WHITE, True)
        self.event_title.pack(pady=(0, 15))
        self.event_description = self._label(content, "", 11, MUTED, justify="center", wraplength=390)
        self.event_description.pack(fill="x", pady=(0, 21))
        self.action_area = tk.Frame(content, bg=PANEL)
        self.action_area.pack(fill="x", side="bottom", pady=(16, 4))
        self.first_button = self._button(self.action_area, "CHIẾN ĐẤU", lambda: self.apply_action("goblin"), primary=True)
        self.first_button.pack(fill="x", pady=(0, 9))
        self.second_button = self._button(self.action_area, "ĐI ĐƯỜNG VÒNG", lambda: self.apply_action("skip"))
        self.second_button.pack(fill="x")
        self.tip_label = self._label(content, "", 10, MUTED, justify="center", wraplength=390)
        self.tip_label.pack(side="bottom", fill="x", pady=(0, 5))

        # Right: journey progress + live log.
        right_card = self._card(main)
        right_card.grid(row=0, column=2, sticky="nsew", padx=(10, 0))
        right = tk.Frame(right_card, bg=PANEL, padx=15, pady=19)
        right.pack(fill="both", expand=True)
        self._label(right, "TIẾN ĐỘ HÀNH TRÌNH", 12, GOLD, True).pack(anchor="w")
        self.progress_label = self._label(right, "0 / 9 sự kiện hoàn tất", 10, MUTED)
        self.progress_label.pack(anchor="w", pady=(8, 6))
        self.progress_bar = tk.Canvas(right, height=10, bg=PANEL_LIGHT, highlightthickness=0)
        self.progress_bar.pack(fill="x")
        self.progress_bar.bind("<Configure>", lambda _: self.update_stats())
        self._label(right, "MỤC TIÊU", 12, GOLD, True).pack(anchor="w", pady=(22, 7))
        self._label(right, "Đánh bại Bowser:\nLevel ≥ 5 và HP ≥ 40", 11, WHITE, justify="left").pack(anchor="w")
        tk.Frame(right, height=1, bg=BORDER).pack(fill="x", pady=18)
        self._label(right, "NHẬT KÝ PHIÊU LƯU", 12, GOLD, True).pack(anchor="w", pady=(0, 10))
        logs = tk.Frame(right, bg=PANEL)
        logs.pack(fill="both", expand=True)
        scrollbar = tk.Scrollbar(logs, width=9)
        scrollbar.pack(side="right", fill="y")
        self.log_box = tk.Text(
            logs, bg="#111B2D", fg=WHITE, font=(FONT, 10),
            bd=0, relief="flat", wrap="word", padx=10, pady=12,
            state="disabled", yscrollcommand=scrollbar.set,
            highlightthickness=0, spacing1=5, spacing3=9,
        )
        self.log_box.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.log_box.yview)
        self.log_box.tag_config("info", foreground=MUTED)
        self.log_box.tag_config("good", foreground=GREEN)
        self.log_box.tag_config("bad", foreground=RED)
        self.log_box.tag_config("todo", foreground=GOLD)

        footer_text = ("BẢN GIÁO VIÊN: GAME CÓ ĐẦY ĐỦ CHỨC NĂNG  •  PYTHON 3 + TKINTER"
                       if getattr(logic, "SOLUTION", False) else
                       "BẢN HỌC VIÊN: HOÀN THÀNH CÁC HÀM TODO TRONG logic.py  •  PYTHON 3 + TKINTER")
        footer = self._label(self.root, footer_text, 9, MUTED)
        footer.pack(pady=(0, 12))

    def write_log(self, text, kind="info"):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", "• " + text + "\n", kind)
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def update_stats(self):
        h = self.hero
        self.hp_label.configure(text=f'{h["hp"]} / {h["max_hp"]}', fg=RED if h["hp"] <= 30 else GREEN)
        for key in self.values:
            self.values[key].configure(text=str(h[key]))
        width = max(1, self.hp_bar.winfo_width())
        self.hp_bar.delete("all")
        self.hp_bar.create_rectangle(0, 0, width * h["hp"] / max(1, h["max_hp"]), 13,
                                     fill=RED if h["hp"] <= 30 else GREEN, outline="")
        count = MAX_SCENES if self.finished and self.result else self.scene
        self.progress_label.configure(text=f"{count} / {MAX_SCENES} sự kiện hoàn tất")
        barwidth = max(1, self.progress_bar.winfo_width())
        self.progress_bar.delete("all")
        self.progress_bar.create_rectangle(0, 0, barwidth * count / MAX_SCENES, 10,
                                           fill=GOLD, outline="")
        self.potion_btn.configure(state="disabled" if self.finished else "normal")

    def restart(self, first_time=False):
        self.hero = new_hero()
        self.scene = 0
        self.finished = False
        self.result = None
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")
        self.write_log("Vua Arthur giao sứ mệnh giải cứu Guinevere.")
        self.write_log("Hãy chọn hành động để bắt đầu hành trình!")
        self.draw_scene()
        if not first_time:
            self.write_log("Đã bắt đầu lại cuộc phiêu lưu.")

    def draw_scene(self):
        if self.finished:
            return
        data = SCENES[self.scene]
        self.step_label.configure(text=f"SỰ KIỆN {self.scene+1:02d} / {MAX_SCENES:02d}")
        self.symbol.configure(text=data["symbol"])
        self.tag.configure(text=data["tag"])
        self.event_title.configure(text=data["title"])
        self.event_description.configure(text=data["description"])
        self.first_button.configure(text=data["primary"][0],
                                    command=lambda a=data["primary"][1]: self.apply_action(a), state="normal")
        self.second_button.configure(text=data["secondary"][0],
                                     command=lambda a=data["secondary"][1]: self.apply_action(a), state="normal")
        self.tip_label.configure(text="Mẹo: Theo dõi HP và vật phẩm ở bảng bên trái.")
        self.update_stats()

    def use_potion(self):
        if self.finished:
            return
        if self.hero["remedy"] <= 0:
            self.write_log("Bạn không có Remedy trong túi.", "bad")
            return
        try:
            result = logic.use_remedy(self.hero)
        except Exception as exc:
            self._show_code_error(exc)
            return
        if self._is_todo(result):
            self.write_log(str(result), "todo")
            return
        self.write_log(str(result), "good")
        self._after_event(advance=False)

    @staticmethod
    def _is_todo(result):
        return not isinstance(result, str) or not result.strip() or result.lstrip().upper().startswith("TODO")

    def _show_code_error(self, exc):
        self.write_log(f"Lỗi trong hàm học viên: {type(exc).__name__}: {exc}", "bad")
        messagebox.showerror("Lỗi trong logic.py", f"{type(exc).__name__}: {exc}\n\nKiểm tra hàm TODO bạn vừa sửa.")

    def apply_action(self, action):
        if self.finished:
            return
        if action == "retreat":
            self.end_game(False, "Hiệp sĩ rút lui. Công chúa vẫn chưa được giải cứu.")
            return
        if action == "skip":
            self.write_log(f"Bỏ qua: {SCENES[self.scene]['title']}.")
            self._after_event(advance=True)
            return
        if action == "phoenix":
            if self.hero["phoenix"] < 3:
                self.hero["phoenix"] += 1
                self.write_log("Nhặt được 1 PhoenixDown.", "good")
            else:
                self.write_log("Túi PhoenixDown đã đầy.")
            self._after_event(advance=True)
            return

        handlers = {
            "goblin": logic.fight_goblin,
            "heal": lambda h: logic.heal(h, 20),
            "bandit": logic.fight_bandit,
            "treasure": logic.take_treasure,
            "buy": logic.buy_remedy,
            "merlin": logic.meet_merlin,
            "troll": logic.fight_troll,
            "bowser": logic.fight_bowser,
        }
        try:
            result = handlers[action](self.hero)
        except Exception as exc:
            self._show_code_error(exc)
            return
        if action == "bowser":
            if type(result) is not bool:
                self.write_log("TODO: fight_bowser() phải trả về True hoặc False (bool).", "todo")
                return
            self.end_game(bool(result), "Bạn chiến thắng Bowser!" if result else "Bạn chưa đủ sức mạnh đánh bại Bowser.")
            return
        if self._is_todo(result):
            self.write_log(str(result) if result is not None else f"TODO: Chưa hoàn thành hàm {action}().", "todo")
            return
        self.write_log(str(result), "good" if self.hero["hp"] > 0 else "bad")
        self._after_event(advance=True)

    def _after_event(self, advance):
        self.update_stats()
        if self.hero["hp"] <= 0:
            self.end_game(False, "Hiệp sĩ đã gục ngã trên hành trình.")
            return
        if advance:
            self.scene += 1
            if self.scene >= MAX_SCENES:
                self.end_game(False, "Hành trình kết thúc mà chưa giải cứu được công chúa.")
            else:
                self.draw_scene()

    def end_game(self, won, message):
        self.finished = True
        self.result = won
        score = (
            self.hero["hp"] + 10 * self.hero["level"] + self.hero["gold"]
            + 5 * self.hero["remedy"] + 15 * self.hero["phoenix"]
        ) if won else -1
        self.step_label.configure(text="KẾT THÚC HÀNH TRÌNH")
        self.symbol.configure(text="♛" if won else "✖", fg=GREEN if won else RED)
        self.event_title.configure(text="GIẢI CỨU THÀNH CÔNG!" if won else "NHIỆM VỤ THẤT BẠI")
        self.tag.configure(text="GUINEVERE ĐƯỢC GIẢI CỨU" if won else "GAME OVER")
        self.event_description.configure(text=f"{message}\n\nĐIỂM CUỐI: {score}\n\nNhấn CHƠI LẠI để thử hành trình mới.")
        self.first_button.configure(state="disabled")
        self.second_button.configure(state="disabled")
        self.tip_label.configure(text="Điểm = HP + 10×Level + Gold + 5×Remedy + 15×PhoenixDown" if won else "Bạn có thể chơi lại và chọn chiến thuật khác.")
        self.write_log(f"{message} Điểm: {score}", "good" if won else "bad")
        self.update_stats()
        messagebox.showinfo("Kết quả hành trình", f"{message}\n\nĐiểm của bạn: {score}")


def main():
    root = tk.Tk()
    Game(root)
    root.mainloop()


if __name__ == "__main__":
    main()
