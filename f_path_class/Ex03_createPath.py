from pathlib import Path
from datetime import datetime
from _datetime import datetime
# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())
print(Path.home())  # 홈 경로 (디렉토리)

p1 = Path('Ex03_createPath.py')
print(p1.stat())

# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기

tm = p1.stat().st_ctime
print(tm)

zt = datetime.fromtimestamp(tm)
print(zt)

# ------------------------------------------------
# 3. 디렉토리 생성
p2 = Path('temp/imsi/test')
p2.mkdir(exist_ok=True, parents=True)  # 있어도 계속 만든다

# ------------------------------------------------
# 4. 파일 생성
path = Path('./temp/a.txt')
f = open(path, 'w', encoding='utf-8')
f.write('홍길동화이팅!')
f.close()

with open('./temp/b.txt', 'a', encoding='utf-8') as f:
    f.write('홍길자화이팅!')

f = Path('./temp/c.txt')
f.touch()
# ------------------------------------------------
#  5. 경로 제거
p = Path('temp/imsi/test')
p.rmdir()  # 비어 있지 않으면 지울 수 없음
