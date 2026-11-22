# BÀI TẬP LỚN PYTHON – GIẢI CỨU CÔNG CHÚA GUINEVERE

**Phiên bản game nhập môn • Lập trình Python sau chương Hàm**  
**Mã bài trên Discord:** `PY120-01` đến `PY120-11`  
**Hình thức:** Cá nhân • **Ngôn ngữ:** Python 3 • **Giao diện:** Tkinter

> Đây là bài tập lớn **tự biên soạn, lấy cảm hứng từ phong cách đề Công chúa Guinevere của HCMUT**. Quy tắc, nhân vật, cơ chế chấm và test case trong tài liệu được thiết kế riêng cho khóa học; không phải đề hay test chính thức của HCMUT.

## I. MỤC TIÊU

Sau bài tập lớn, học viên cần chứng minh khả năng kết hợp biến, biểu thức, câu lệnh điều kiện, vòng lặp, dictionary, hàm, tham số và `return` để xây dựng chương trình có nhiều chức năng phối hợp. Học viên phải xử lý đúng giới hạn chỉ số, tình huống biên và chuỗi sự kiện liên tiếp; không chỉ làm đúng một vài ví dụ.

**Phần đã có sẵn:** toàn bộ giao diện, màn hình thông tin, nút hành động, 9 sự kiện cốt truyện, nhật ký, điểm số và kết nối với hàm logic. **Phần học viên cần làm:** hoàn thiện đúng 10 hàm `TODO` trong `logic.py`. Không sửa `main.py` hoặc `bridge_template.txt`.

## II. BỐI CẢNH VÀ NHIỆM VỤ

Công chúa **Guinevere** bị rồng **Bowser** bắt giữ trong lâu đài. Vua Arthur giao cho một hiệp sĩ thực hiện chuyến giải cứu. Trên đường đi, hiệp sĩ chạm trán Goblin, Bandit, Troll; tìm kho báu; mua Remedy; gặp Merlin và thu thập PhoenixDown. Các quyết định làm thay đổi sức khỏe, cấp độ, vàng và vật phẩm. Mục tiêu cuối cùng là đánh bại Bowser và đưa công chúa về vương quốc.

### 1. Trạng thái nhân vật

| Khóa trong `hero` | Ý nghĩa | Giá trị ban đầu | Giới hạn |
|---|---|---:|---|
| `hp` | Điểm sức khỏe hiện tại | 100 | `0 .. max_hp` sau xử lý |
| `max_hp` | Sức khỏe tối đa | 100 | Không thay đổi |
| `level` | Cấp độ chiến đấu | 2 | `1 .. 10` |
| `gold` | Tiền vàng | 15 | `0 .. 100` |
| `remedy` | Số thuốc hồi phục | 1 | `0 .. 5` |
| `phoenix` | Số vật phẩm hồi sinh | 0 | `0 .. 3` |

Game tạo nhân vật ban đầu bằng dictionary; **các test case có thể khởi tạo nhân vật với trạng thái khác để kiểm tra giới hạn**. Mọi hàm nhận `hero` và cập nhật trực tiếp các khóa cần thiết của dictionary đó.

### 2. Luật chiến thắng và tính điểm

- Giải cứu thành công khi đến sự kiện Bowser và hàm `fight_bowser(hero)` trả về `True` với **`level >= 5` đồng thời `hp >= 40`**.
- Thất bại nếu HP giảm về 0 mà không có PhoenixDown, hoặc người chơi rút lui, hoặc không thỏa điều kiện khi đối đầu Bowser.
- PhoenixDown được sử dụng **tự động** trong `take_damage` nếu HP sau sát thương <= 0. Một PhoenixDown bị tiêu hao; HP được đặt thành `max(1, max_hp // 2)`.
- Điểm kết thúc: nếu chiến thắng, `score = hp + 10*level + gold + 5*remedy + 15*phoenix`; nếu thua, `score = -1`.

## III. CÁCH CHƠI GAME

**Bước 1.** Giải nén gói học viên; mở thư mục có `main.py` và `logic.py` bằng VS Code.  
**Bước 2.** Chạy lệnh `python main.py` (trên Windows có thể dùng `py main.py`). Máy phải cài Python có Tkinter.  
**Bước 3.** Quan sát bảng thông tin bên trái, đọc tình huống ở giữa và chọn nút hành động tương ứng.  
**Bước 4.** Kiểm tra nhật ký và các chỉ số sau hành động. Hệ thống hiển thị thông báo `TODO` khi hàm liên quan chưa được hoàn thiện; lúc đó cần sửa `logic.py` rồi mở lại game.  
**Bước 5.** Tại màn hình cuối, chọn **Đối đầu Bowser**. Nếu chưa đủ điều kiện, có thể dùng Remedy (nếu còn) trước trận. Khi kết thúc, game hiển thị thắng/thua và điểm tổng kết.

### Hành trình gồm 9 màn chơi

| Sự kiện | Lựa chọn chính | Hàm được gọi / tác động |
|---|---|---|
| 1. Rừng sương mù | Chiến đấu Goblin / đi đường vòng | `fight_goblin(hero)` |
| 2. Suối ánh trăng | Uống nước suối / bỏ qua | `heal(hero, 20)` |
| 3. Bọn cướp đường | Đánh Bandit / tránh | `fight_bandit(hero)` |
| 4. Rương kho báu | Mở rương / rời đi | `take_treasure(hero)` |
| 5. Cửa hàng du mục | Mua thuốc / không mua | `buy_remedy(hero)` |
| 6. Phù thủy Merlin | Nhận chúc phúc / từ chối | `meet_merlin(hero)` |
| 7. Cổng đá Troll | Chiến đấu / tránh | `fight_troll(hero)` |
| 8. Kho dự trữ cổ | Nhặt PhoenixDown / bỏ qua | Tăng 1 `phoenix`, tối đa 3 (xử lý sẵn trong giao diện) |
| 9. Lâu đài Bowser | Đối đầu / rút lui | `fight_bowser(hero)` |

**Nút dùng thuốc:** dùng được trong hành trình khi có Remedy, gọi `use_remedy(hero)`; không tự chuyển sang màn kế. Các lựa chọn bỏ qua/đi đường vòng không thay đổi chỉ số và chuyển sang màn tiếp theo. Người chơi chỉ có 1 lượt thăm mỗi màn trong một lần chơi.

## IV. ĐẶC TẢ 10 HÀM CẦN HOÀN THÀNH

### TODO 01 — `heal(hero, amount)` | Hồi sức khỏe

**Vai trò:** Cập nhật HP khi uống nước suối, dùng thuốc hoặc nhận phép thuật của Merlin.

- Nhận dictionary `hero` và số nguyên `amount`.
- Đặt `hero["hp"] = min(hero["max_hp"], hero["hp"] + amount)`.
- Không thay đổi chỉ số khác. Trả về **chuỗi mô tả không rỗng**, ví dụ “Hồi 10 HP”.
- Ví dụ: HP=95, MaxHP=100, `amount=20` thì HP mới là **100**, không phải 115.

### TODO 02 — `take_damage(hero, amount)` | Sát thương và hồi sinh

**Vai trò:** Xử lý mọi đòn tấn công gây sát thương trong game; các hàm chiến đấu cần gọi lại hàm này.

- Trừ `amount` khỏi HP.
- Nếu HP > 0: giữ HP đã trừ, không mất PhoenixDown.
- Nếu HP <= 0 và `phoenix > 0`: giảm PhoenixDown đi 1; gán HP thành `max(1, max_hp // 2)`.
- Nếu HP <= 0 và `phoenix == 0`: đặt HP = 0.
- Trả về chuỗi mô tả sát thương/hồi sinh, không dùng `print()`.
- Ví dụ: HP=15, MaxHP=100, PhoenixDown=1, sát thương=20 → HP=50, PhoenixDown=0.

### TODO 03 — `fight_goblin(hero)` | Chiến đấu Goblin

**Vai trò:** Kiểm tra cách dùng lại hàm `take_damage`, toán tử `max` và cập nhật nhiều chỉ số.

- Tính sát thương: `damage = max(4, 18 - 2*level)`.
- Gọi `take_damage(hero, damage)`.
- Nếu HP sau xử lý > 0 (bao gồm trường hợp vừa hồi sinh): nhận +10 Gold (tối đa 100), +1 Level (tối đa 10).
- Nếu HP = 0: không nhận thưởng.
- Trả về chuỗi thông báo kết quả.
- Ví dụ: Level=2, HP=90, Gold=15 → sát thương 14; HP=76, Level=3, Gold=25.

### TODO 04 — `fight_bandit(hero)` | Chiến đấu Bandit

**Vai trò:** Sử dụng nhánh điều kiện theo cấp độ và giới hạn tiền vàng.

- Nếu `level >= 3`: gọi `take_damage(hero, 8)`; nếu HP sau xử lý > 0 thì +15 Gold và +1 Level (có giới hạn).
- Nếu `level < 3`: gọi `take_damage(hero, 20)`; sau đó trừ 10 Gold, thấp nhất là 0; không tăng Level.
- Nếu HP=0 sau trận, game kết thúc thất bại.
- Trả về chuỗi mô tả, không `print()`.

### TODO 05 — `take_treasure(hero)` | Mở kho báu

**Vai trò:** Rèn luyện phép cộng và điều kiện chặn giá trị tối đa.

- Cộng 20 Gold; Gold sau cùng không vượt quá 100.
- Các chỉ số khác không thay đổi.
- Ví dụ: Gold=93 → Gold mới=100 (không phải 113).
- Trả về chuỗi mô tả.

### TODO 06 — `buy_remedy(hero)` | Mua thuốc

**Vai trò:** Kiểm tra điều kiện kép.

- Chỉ mua nếu `gold >= 15` và `remedy < 5`.
- Mua thành công: Gold giảm 15, Remedy tăng 1.
- Nếu không đủ vàng hoặc túi đã có 5 Remedy: giữ nguyên mọi chỉ số.
- Trả về chuỗi mô tả mua thành công/thất bại.

### TODO 07 — `use_remedy(hero)` | Sử dụng thuốc

**Vai trò:** Kết hợp điều kiện tồn kho và gọi lại `heal`.

- Nếu `remedy >= 1`: trừ 1 Remedy, hồi 40 HP (không vượt quá MaxHP).
- Nếu không có Remedy: giữ nguyên chỉ số.
- Có thể gọi `heal(hero, 40)` để tránh viết lại logic.
- **Ngay cả khi HP đã đầy**, nếu chọn dùng thuốc và còn thuốc thì vẫn tiêu hao 1 Remedy.
- Trả về chuỗi mô tả.

### TODO 08 — `meet_merlin(hero)` | Nhận chúc phúc

**Vai trò:** Nâng cấp nhân vật và sử dụng lại hàm hồi phục.

- Tăng 1 Level, tối đa 10.
- Hồi 10 HP, tối đa MaxHP.
- Có thể gọi `heal(hero, 10)`.
- Trả về chuỗi mô tả.

### TODO 09 — `fight_troll(hero)` | Đánh quỷ Troll

**Vai trò:** Phối hợp điều kiện, sát thương, hồi sinh và phần thưởng.

- Nếu `level >= 4`: nhận 18 sát thương bằng `take_damage`; nếu HP sau xử lý > 0, +25 Gold (tối đa 100) và +1 Level (tối đa 10).
- Nếu `level < 4`: nhận 35 sát thương bằng `take_damage`; không nhận thưởng và không tăng Level.
- Trả về chuỗi mô tả. Trường hợp được hồi sinh và còn HP vẫn nhận phần thưởng ở nhánh thắng.

### TODO 10 — `fight_bowser(hero)` | Trận chiến cuối

**Vai trò:** Kiểm tra điều kiện thắng và giá trị trả về kiểu boolean.

- Trả về **đúng kiểu `bool`**, bằng `True` khi `level >= 5 and hp >= 40`, ngược lại `False`.
- Không thay đổi bất kỳ chỉ số nào trong `hero`.
- Không in kết quả, không trả chuỗi `'True'`/`'False'`, số 1/0 hoặc `None`.
- Ví dụ: Level=5 và HP=40 → `True`; Level=5 và HP=39 → `False`.

## V. YÊU CẦU CHUNG VỀ CÁC HÀM

1. Giữ nguyên **tên hàm, thứ tự tham số** và 6 khóa của dictionary `hero`.
2. Chỉ viết thuật toán bên trong các hàm đánh dấu `TODO` ở `logic.py`.
3. Chín hàm đầu phải trả về một chuỗi **không rỗng, không bắt đầu bằng “TODO”**; nội dung câu chữ có thể khác ví dụ. `fight_bowser` phải trả về `bool`.
4. Không dùng `input()` hoặc `print()` trong các hàm. Các thông báo hiển thị được game xử lý.
5. Các test kiểm tra trạng thái **sau mỗi lần gọi**, kể cả chuỗi nhiều hàm liên tiếp; không tự tạo lại `hero` bên trong hàm.
6. Không cần class, OOP, Pygame hoặc thư viện bên ngoài. Có thể dùng các hàm có sẵn `min`, `max`, và các cấu trúc Python cơ bản.

## VI. VÍ DỤ TỰ KIỂM TRA

**Tình huống A – hồi vượt giới hạn:** `hero = {"hp":95,"max_hp":100,"level":2,"gold":15,"remedy":1,"phoenix":0}`; gọi `heal(hero,20)` → HP=100 và những chỉ số khác không đổi.

**Tình huống B – bị đánh và hồi sinh:** `hero = {"hp":12,"max_hp":100,"level":2,"gold":15,"remedy":1,"phoenix":1}`; gọi `take_damage(hero,20)` → HP=50, PhoenixDown=0.

**Tình huống C – điều kiện Bowser:** `hero = {"hp":40,"max_hp":100,"level":5,"gold":15,"remedy":0,"phoenix":0}`; gọi `fight_bowser(hero)` → `True` và không đổi `hero`.

**Tình huống D – nhiều hành động:** khởi đầu HP=90, MaxHP=100, Level=2, Gold=15, Remedy=1, PhoenixDown=0. Thực hiện `fight_goblin` → HP=76, Level=3, Gold=25; tiếp theo `use_remedy` → HP=100, Remedy=0; tiếp theo `fight_bowser` → `False` (Level chưa đủ 5).

## VII. CHẤM BÀI TRÊN DISCORD

### 1. Tổ chức bộ đề

| Mã đề | Nội dung | Số test | Công khai | Ẩn |
|---|---|---:|---:|---:|
| PY120-01 | `heal` | 21 | 4 | 17 |
| PY120-02 | `take_damage` | 21 | 4 | 17 |
| PY120-03 | `fight_goblin` | 21 | 4 | 17 |
| PY120-04 | `fight_bandit` | 21 | 4 | 17 |
| PY120-05 | `take_treasure` | 21 | 4 | 17 |
| PY120-06 | `buy_remedy` | 21 | 4 | 17 |
| PY120-07 | `use_remedy` | 21 | 4 | 17 |
| PY120-08 | `meet_merlin` | 21 | 4 | 17 |
| PY120-09 | `fight_troll` | 21 | 4 | 17 |
| PY120-10 | `fight_bowser` | 21 | 4 | 17 |
| PY120-11 | Hành trình tổng hợp | 20 | 0 | 20 |
| **TỔNG** | | **230** | **40** | **190** |

### 2. Lệnh Discord

- `/guinevere`: nhận file hướng dẫn bài tập lớn.
- `/danhsach buoi:120`: xem 11 đề Guinevere.
- `/de bai:PY120-01`: xem tên đề, yêu cầu và một ví dụ công khai.
- `/testcase ten:PY120-01:01` + tệp `.py`: chấm riêng test 01; **không tính điểm vào bảng điểm**.
- `/nopbai bai:PY120-01` + tệp `.py`: chấm toàn bộ 21 test của hàm 01, ghi điểm theo số test đạt. `PY120-11` có 20 test.

Các test ẩn vẫn được chạy nhưng học viên chỉ nhìn thấy trạng thái Accepted / Wrong Answer / Runtime Error / Time Limit Exceeded. Giáo viên có quyền quản trị mới được xem input/output chi tiết của test ẩn trong báo cáo.

### 3. Cách tạo file nộp

**Không nộp `main.py` của giao diện Tkinter** vì Discord Judge chạy code ở môi trường không có cửa sổ. Học viên sử dụng công cụ được cấp sẵn:

```text
python build_submission.py
```

Lệnh trên tạo `main_nop_discord.py` gồm **10 hàm học viên đã viết và mã kết nối chấm bài**. Sau mỗi lần sửa `logic.py`, phải chạy lại lệnh này để cập nhật file nộp. Chỉ đính kèm `main_nop_discord.py` khi dùng `/testcase` hoặc `/nopbai`. Giáo viên giữ `data/dataset.zip` (có test ẩn) trên VPS, không phát tệp này cho học viên.

### 4. Chạy test tại máy học viên

```text
python run_tests.py --file logic.py --suite public
```

Chương trình kiểm tra 40 ca công khai. Bộ test ẩn chỉ chạy trên Discord Judge của giáo viên; không gửi bộ test ẩn qua kênh công khai.

## VIII. CƠ CHẾ CHẤM VÀ TIÊU CHÍ ĐÁNH GIÁ

Mỗi test của từng đề được chấm **đúng/sai** bằng cách so sánh 6 chỉ số sau hành động; đồng thời kiểm tra kết quả trả về đúng kiểu quy định. Một đề đạt 21/21 hoặc 20/20 test tương ứng 100/100 điểm của đề đó. Bài tổng hợp chỉ đạt khi nhiều hàm phối hợp đúng theo trình tự trong cùng một hành trình.

**Thang đánh giá tham khảo cho BTL:** 50% kết quả 10 đề hàm; 30% hành trình tổng hợp; 10% chạy game và trình bày; 10% giải thích thuật toán. Giáo viên có thể điều chỉnh, đây không phải công thức tự động của bot (bot lưu điểm riêng từng đề).

## IX. CẤU TRÚC NỘP BÀI VÀ LƯU Ý

- **Chạy game:** `main.py`, `logic.py` và các file game cấp sẵn trong cùng thư mục.
- **Bài làm:** chỉ thay nội dung TODO trong `logic.py`.
- **Nộp lên Discord:** tạo lại và nộp `main_nop_discord.py`.
- **Test công khai:** sử dụng `run_tests.py` và `cases_public.json`.
- **Kiểm tra:** thử trường hợp HP vừa bằng 0; vàng đúng 15; thuốc vừa đầy 5; Level vừa 10; HP đúng 40; và nhiều hàm chạy liên tục.

**Không chia sẻ tài khoản Discord, mã thông báo bot hoặc dữ liệu test ẩn.** Học viên phải tự hoàn thiện thuật toán và có thể được yêu cầu giải thích công dụng từng hàm.

---

*Bản đặc tả dành cho BTL Python Guinevere, phù hợp giao diện game và 230 test của khóa học.*
