"""Gộp logic.py + cầu nối chấm bài vào một file main_nop_discord.py."""
from pathlib import Path
import ast
import sys
base = Path(__file__).resolve().parent
source_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else base / 'logic.py'
target_path = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else base / 'main_nop_discord.py'
source = source_path.read_text(encoding='utf-8-sig')
ast.parse(source)  # Stop early on syntax errors.
bridge = (base / 'bridge_template.txt').read_text(encoding='utf-8')
if '_guinevere_discord_main' in source:
    raise SystemExit('logic.py đã chứa mã chấm bài, hãy chỉ viết 10 hàm TODO.')
target_path.write_text(source.rstrip()+'\n\n'+bridge, encoding='utf-8')
print(f'Đã tạo file nộp Discord: {target_path} ({target_path.stat().st_size} bytes)')
print('Chỉ gửi file này vào lệnh /nopbai; file main.py giao diện không dùng để nộp.')
