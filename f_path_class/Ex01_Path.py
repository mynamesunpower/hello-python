"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path

# (1) 해당 경로와 하위 목록들 확인
p = Path(r'c:\Windows')
print(p)
print(p.resolve())  # Path에 해당하는 절대 경로
print('---------------------------------')

test = []
for x in p.iterdir():
    if x.is_dir():
        test.append(x)
print(test)

# [복습]
test2 = [x for x in p.iterdir() if x.is_dir()]
print(test2)

print('---------------------------------')
p = Path('.')
print(p.absolute())
subs = list(p.glob('*.py'))
print(subs)

print(list(Path(r'../a_datatype_class/').glob('*.txt')))
print(list(Path('.').glob('../a_datatype_class/*.txt')))