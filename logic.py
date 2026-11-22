"""BÀI TẬP LỚN PYTHON: GIẢI CỨU CÔNG CHÚA GUINEVERE.

CHỈ SỬA FILE NÀY. Giao diện và cốt truyện đã lập trình sẵn trong main.py.

hero là một dictionary chứa:
    hero["hp"]       : HP hiện tại
    hero["max_hp"]   : HP tối đa
    hero["level"]    : cấp độ, tối đa 10
    hero["gold"]     : vàng, từ 0 đến 100
    hero["remedy"]   : số thuốc, từ 0 đến 5
    hero["phoenix"]  : số vật phẩm hồi sinh, từ 0 đến 3

Quy tắc: Mỗi hàm (trừ fight_bowser) cập nhật hero và trả về
một chuỗi ngắn mô tả kết quả để hiển thị trong nhật ký.
Không print() trong các hàm bên dưới.

GỢI Ý: Để kiểm tra, chạy: python -m unittest -v test_logic
"""


SOLUTION = False


def heal(hero, amount):
    """TODO 01 (dễ): Hồi amount HP, nhưng không vượt quá max_hp.

    Ví dụ: hp=90, max_hp=100, amount=20 -> hp=100.
    Trả về chuỗi mô tả việc hồi phục.
    """
    # TODO: Học viên tự viết.
    return "TODO 01: Chưa lập trình hàm heal()."


def take_damage(hero, amount):
    """TODO 02 (trung bình): Trừ HP khi bị tấn công.

    - Nếu sau sát thương HP > 0: giữ HP đó.
    - Nếu HP <= 0 và có PhoenixDown: trừ 1 PhoenixDown,
      hồi sinh với HP = max(1, max_hp // 2).
    - Nếu HP <= 0 và không có PhoenixDown: HP = 0.
    Trả về chuỗi mô tả sát thương và (nếu có) hồi sinh.
    """
    # TODO: Học viên tự viết.
    return "TODO 02: Chưa lập trình hàm take_damage()."


def fight_goblin(hero):
    """TODO 03 (trung bình): Đánh yêu tinh Goblin.

    - Sát thương = max(4, 18 - 2 * level).
    - Sử dụng take_damage(hero, damage).
    - Nếu còn HP sau trận: +10 Gold (tối đa 100), +1 Level (tối đa 10).
    Trả về chuỗi mô tả kết quả giao chiến.
    """
    # TODO: Học viên tự viết.
    return "TODO 03: Chưa lập trình hàm fight_goblin()."


def fight_bandit(hero):
    """TODO 04 (trung bình): Đánh bọn cướp Bandit.

    - Nếu Level >= 3: nhận 8 sát thương; nếu sống sót,
      +15 Gold (tối đa 100), +1 Level (tối đa 10).
    - Nếu Level < 3: nhận 20 sát thương và mất 10 Gold
      (Gold không được âm).
    - Sử dụng hàm take_damage().
    Trả về chuỗi kết quả.
    """
    # TODO: Học viên tự viết.
    return "TODO 04: Chưa lập trình hàm fight_bandit()."


def take_treasure(hero):
    """TODO 05 (dễ): Nhận 20 Gold, tối đa 100 Gold.

    Trả về chuỗi kết quả.
    """
    # TODO: Học viên tự viết.
    return "TODO 05: Chưa lập trình hàm take_treasure()."


def buy_remedy(hero):
    """TODO 06 (dễ): Mua 1 Remedy với giá 15 Gold.

    Chỉ được mua khi gold >= 15 và remedy < 5.
    Nếu không đủ vàng hoặc đầy túi: giữ nguyên chỉ số.
    Trả về chuỗi kết quả.
    """
    # TODO: Học viên tự viết.
    return "TODO 06: Chưa lập trình hàm buy_remedy()."


def use_remedy(hero):
    """TODO 07 (dễ): Dùng thuốc Remedy trong túi.

    Nếu có thuốc: giảm remedy đi 1, hồi 40 HP (không vượt max_hp).
    Nếu không có: không thay đổi chỉ số.
    Có thể sử dụng hàm heal().
    Trả về chuỗi kết quả.
    """
    # TODO: Học viên tự viết.
    return "TODO 07: Chưa lập trình hàm use_remedy()."


def meet_merlin(hero):
    """TODO 08 (dễ): Nhận lời chúc phúc của Merlin.

    +1 Level (tối đa 10), hồi 10 HP (không vượt max_hp).
    Có thể gọi lại hàm heal().
    Trả về chuỗi kết quả.
    """
    # TODO: Học viên tự viết.
    return "TODO 08: Chưa lập trình hàm meet_merlin()."


def fight_troll(hero):
    """TODO 09 (khá): Đánh quỷ Troll.

    - Nếu Level >= 4: nhận 18 sát thương; nếu sống sót,
      +25 Gold (tối đa 100), +1 Level (tối đa 10).
    - Nếu Level < 4: nhận 35 sát thương, không nhận thưởng.
    - Sử dụng hàm take_damage().
    Trả về chuỗi kết quả.
    """
    # TODO: Học viên tự viết.
    return "TODO 09: Chưa lập trình hàm fight_troll()."


def fight_bowser(hero):
    """TODO 10 (dễ): Trận đấu cuối cùng.

    Trả về True khi level >= 5 VÀ hp >= 40, ngược lại False.
    KHÔNG thay đổi các chỉ số của hero.
    """
    # TODO: Học viên tự viết.
    return None  # TODO: Thay None bằng điều kiện thắng/thua.
