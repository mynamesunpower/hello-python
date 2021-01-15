
# 1
with open('sample.txt', 'r') as file:
    sum = 0
    score_list = file.read().split('\n')
    for i in score_list:
        sum += int(i)
    print(f'총합: {sum}, 평균: {sum/len(score_list)}')

# 2
with open('dream.txt', 'r', encoding='UTF-8') as file:
    content = file.read()
    for index, row in enumerate(content.split('\n')):
        print(f'{index}---{row}')

    # 3 (이어서)
    words = content.split()
    lines = content.split('\n')
    print(f'총 글자의 수 : {len(content)}')
    print(f'총 단어의 수 : {len(words)}')
    print(f'총 단어의 수 : {len(lines)}')

# 4
from random import randint
from pathlib import *
from datetime import datetime

path = Path(r'.')
logtemp = Path(r'logtemp/')

for child_path in path.iterdir():
    if not logtemp.is_dir():
        logtemp.mkdir()

with open('./logtemp/temp_log.txt', 'a', encoding='UTF-8') as file:
    ct = datetime.fromtimestamp(Path(r'logtemp/temp_log.txt').stat().st_ctime)
    for i in range(10):
        file.write(f'{str(randint(1, 100))}, {ct}\n')
