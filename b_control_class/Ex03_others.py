msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

# 1. unpacking : 각 요소를 하나씩 분해
c1, c2, c3 = di.items()
print(c1, c2, c3)

for (key, value) in di.items():
    print(key, ':', value)

alist = [(1, 2), (3, 4), (5, 6)]
for (a, b) in alist:
    # alist라는 리스트 (Collection)에서 추출한 요소가 (a, b) 형식의 튜플이다
    # 그 튜플에서 다시 a, b로 분해해서 각각의 변수에 지정한다.
    print(a+b)

for i in range(len(alist)):
    print(i, '번째 튜플의 합:', alist[i][0] + alist[i][1])

print(list((a + b) for (a, b) in alist))

# 2. enumerate()
# index와 값을 튜플의 형태로 반환해준다.
user_list = ['개발자', '코더', '전문가', '분석가']

for value in user_list:
    print(value)

print(list(value for value in user_list))

for index, value in enumerate(user_list):
    # print(type(index)) <class 'int'>
    print(index, ':', value)

print(list((index, value) for index, value in enumerate(user_list)))

# 3. zip() ******************
# 리스트의 길이가 같다면 zip() 함수를 이용하여 데이터를 하나로 묶을 수 있다.
days = ['월', '화', '수']
doit = ['잠자기', '밥먹기', '공부하기']

print(zip(days, doit))
print(list(zip(days, doit)))
print(dict(zip(days, doit)))

for (days, do) in zip(days, doit):
    print('{}요일에는 {}를 합니다'.format(days, do))
