# Ex02_csv.py

# 1. 리스트의 데이터를 csv로 저장
import csv

data = [[1, '김길동', '책임'], [2, '박길동', '연구원'], [3, '최길동', '선임']]
with open('./data/imsi.csv', 'wt', newline='', encoding='UTF-8-sig') as f:
    cout = csv.writer(f)
    cout.writerow(data)

with open('./data/imsi.csv', 'r', encoding='utf-8-sig') as f:
    cin = csv.reader(f)
    data = [row for row in cin]
print(data)