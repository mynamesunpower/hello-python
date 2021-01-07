
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1', '2', '3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in b:
    print(entry, type(entry))

for entry in e:  # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry, e[entry], type(entry))

for entry in e.items():
    print(entry)

# [연습] 1부터 10까지의 합을 출력
sum = 0
for number in range(1, 11):
    sum += number
print(sum)

# 홀수의 합을 출력
sum = 0
for number in range(1, 11, 2):
    sum += number
print(sum)

# 구구단 출력
for dan in range(1, 10):
    for number in range(2, 10):
        print('{} * {} = {:2d}'.format(number, dan, number * dan), end=' | ')
    print()




# =========================================================
# while  ( 안해도 될듯 )

# a = 1
# while True:  # 무한루프
#    if a == 1:
#        print(a)
#        break



"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
