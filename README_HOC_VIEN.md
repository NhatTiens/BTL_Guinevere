# GAME GIẢI CỨU CÔNG CHÚA GUINEVERE — HỌC VIÊN

**Bài tập lớn Python sau khi học xong hàm — Bài học 120 trên Discord.**

## 1. Cấu trúc source

- `main.py`: game Tkinter đã hoàn thiện giao diện 9 màn (chỉ chạy, không sửa).
- `logic.py`: **10 hàm TODO**; đây là file duy nhất học viên cần viết.
- `build_submission.py`: tạo bài nộp theo chuẩn bot Discord.
- `bridge_template.txt`: cầu nối JSON cho bộ chấm, **không sửa**.
- `kiem_tra_discord.py`: tự thử chính xác 40 test công khai từ bot.
- `tests/public.json`: 40 test công khai; **không có test ẩn**.
- `tai_lieu/De_BTL_Guinevere.docx` và `.md`: đề bài, luật chơi, vai trò từng hàm.

## 2. Làm bài và chơi game

Mở CMD/PowerShell tại thư mục giải nén:

```bash
python main.py
```

Quan sát thanh HP, Level, Gold, Remedy, PhoenixDown, mục tiêu và nhật ký.
Ban đầu các chức năng sẽ hiển thị thông báo TODO nếu chưa viết hàm. Bạn **chỉ sửa `logic.py`**, đóng và mở lại game để chạy phiên bản mới.

## 3. Chạy test và nộp bài Discord

```bash
python build_submission.py
python kiem_tra_discord.py
```

File sinh ra là **`main_nop_discord.py`** — đây là file duy nhất cần gửi lên bot, **không phải `logic.py` hay `main.py` của game**.

Trong Discord dùng `/danhsach buoi:120`, `/de bai:PY120-01`, sau đó `/nopbai bai:PY120-01 tep:<file>` và chọn `main_nop_discord.py` làm tệp đính kèm. Có thể nộp cùng một file cho `PY120-01` tới `PY120-11`. Bạn phải **chạy lại lệnh build sau mỗi lần sửa logic.py**.

- Bài `PY120-01` ... `PY120-10`: 21 test/mã (4 công khai + 17 ẩn).
- Bài `PY120-11`: 20 test ẩn, kiểm tra chuỗi nhiều hàm.
- Chỉ giáo viên có test ẩn. Điểm cuối cùng do bot Discord chấm.

**Lưu ý:** Không sử dụng `print()` hoặc `input()` trong 10 hàm TODO. Chín hàm đầu trả về chuỗi không rỗng, không bắt đầu bằng TODO. `fight_bowser` trả về **kiểu bool**, không phải chuỗi hoặc 0/1. Các chỉ số cập nhật trực tiếp trong dictionary `hero`.

Nếu chưa có Python trên Windows, cài Python 3 với Tkinter và mở lại terminal. Không cần cài `pip` hoặc Pygame.

> Đề bài giáo dục tự biên soạn, lấy cảm hứng từ phong cách bài tập lớn Guinevere HCMUT; không phải bộ đề/test chính thức của HCMUT.
