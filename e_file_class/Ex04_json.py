# Ex04_json.py

import json

f = open('./data/temp.json', 'r', encoding='utf-8')
data = f.read()
print(type(data))  # str

print('-'*50)

items = json.loads(data)
print(items)
print(type(items))
employees = items

for item in items:
    print('이름: {}, 번호: {}, 직책: {}'.format(item, items[item]['No'], items[item]['Job']))

for item in items:
    print('이름:', item)
    for prop in items[item]:
        print(prop+':', items[item][prop])
    print('-' * 10)