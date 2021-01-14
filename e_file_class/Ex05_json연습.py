"""
sample.json 파일을 읽어서 총 합을 출력해주세요
"""

import json
try:
    file = open('./data/sample.json', 'r', encoding='UTF-8')
except Exception as e:
    print('예외: ', e)
else:
    with file:
        json_file = json.loads(file.read())
        total_sum, total_price = 0, 0
        for name, props in json_file.items():
            for key, value in props.items():
                if key == 'count':
                    total_sum += int(value)
                else:
                    total_price += int(value)
        print('총 개수: {0}\n총 가격: {1}'.format(total_sum, total_price))
