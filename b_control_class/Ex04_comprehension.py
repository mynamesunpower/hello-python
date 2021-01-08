"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컴프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컴프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컴프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

"""


# 컴프리핸션 사용하지 않은 리스트 생성
a_list = []
a_list.append(1)
a_list.append(2)
a_list.append(3)
a_list.append(4)
a_list.append(5)
a_list.append(6)
print(a_list)

a_list = []
for n in range(1, 7):
    a_list.append(n)
print(a_list)

a_list = list(range(1, 7))
print(a_list)


#------------------------------------------------
# 리스트 컴프리핸션
b_list = [i for i in range(1, 7)]
print(b_list)

b_list = [i + 10 for i in range(1, 7)]
print(b_list)

b_list = [n for n in range(1, 7) if n % 2 == 1]
print(b_list)

# [ 참고 ]
c_list = [(r, c) for r in range(1, 4) for c in range(1, 3)]
print(c_list)

c_list = list()
for r in range(1, 4):
    for c in range(1, 3):
        c_list.append((r, c))
print(c_list)

#-------------------------------------------
# 딕셔러니 컴프리핸션
datas = (2, 3, 4)
adic = {n: n**2 for n in datas}
print(adic)

# 진짜 파이썬한 코드
word = 'LOVE LOL'
wcnt = {letter: word.count(letter) for letter in word}
# 중복제거 set으로 하면서 정렬하기 도전.
import operator
wcnt_2 = sorted(wcnt.items(), key=operator.itemgetter(0))
print(wcnt_2)

#------------------------------------------------
# 셋 컴프리핸션
a_set = set(n for n in range(1, 7))
print(a_set)

b_set = set(a_list)
print(b_set)

datas = [1, 2, 3, 2, 1, 4, 5]
c_set = set(n for n in datas)
print(c_set)

d_set = set(datas)
print(d_set)


# -------------------------------------------------
# [참고] 제너레이터 컨프리핸션
# ( ) 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.
