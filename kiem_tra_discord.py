"""Kiểm tra file nộp giống quy tắc chuẩn hóa stdout của Discord Judge Bot.
Chạy: python kiem_tra_discord.py  (40 test public)
Bản giảng viên: python kiem_tra_discord.py --all
Chỉ dùng thư viện chuẩn; mỗi test chạy trong một tiến trình Python độc lập.
"""
from pathlib import Path
import argparse
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def normalize(text):
    return "\n".join(line.rstrip() for line in text.strip().splitlines())

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--all", action="store_true", help="Chỉ bản giáo viên có 230 test")
    p.add_argument("--file", default="main_nop_discord.py")
    p.add_argument("--problem", default=None, help="Ví dụ PY120-01")
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args()
    data_path = ROOT / 'tests' / ('all_230.json' if args.all else 'public.json')
    if not data_path.exists():
        print('Bản học viên chỉ có test công khai; test ẩn thuộc giáo viên.')
        return 2
    path = (ROOT / args.file).resolve()
    if not path.is_file():
        print('Thiếu file nộp:', path.name)
        print('Hãy chạy python build_submission.py trước.')
        return 2
    cases = json.loads(data_path.read_text(encoding='utf-8'))
    if args.problem:
        cases = [c for c in cases if c['problem_id'].upper()==args.problem.upper()]
    if not cases:
        print('Không có test phù hợp.')
        return 2
    passed=0
    grouped={}
    for case in cases:
        pid=case['problem_id']; number=case['case_number']
        try:
            result=subprocess.run([sys.executable,'-I','-B',str(path)],
                input=case['input'],capture_output=True,text=True,encoding='utf-8',
                timeout=6, cwd=ROOT)
            accepted=result.returncode==0 and normalize(result.stdout)==normalize(case['output'])
            reason= ('Accepted' if accepted else
                     ('Runtime Error: '+result.stderr.strip()[:200] if result.returncode else
                      'Wrong Answer'))
        except subprocess.TimeoutExpired:
            accepted=False; reason='Time Limit Exceeded'
        ok,total=grouped.get(pid,(0,0)); grouped[pid]=(ok+int(accepted),total+1)
        passed+=int(accepted)
        if args.verbose or not accepted:
            print(f"{'PASS' if accepted else 'FAIL'}  {pid}:{number:02d}  {reason}")
    print('\nKẾT QUẢ THEO MÃ ĐỀ')
    for pid,(ok,total) in grouped.items():
        print(f'  {pid}: {ok}/{total}')
    print(f'\nTỔNG: {passed}/{len(cases)} test đạt')
    return 0 if passed==len(cases) else 1

if __name__ == '__main__':
    sys.exit(main())
