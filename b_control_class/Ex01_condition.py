"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0
i2 = 0.0
i3 = ""
i4 = str()
i5 = list()
i6 = tuple()
i7 = set()
i8 = dict()
i9 = {}
i10 = None

if not i:
    print('True2')  # O

a = 2
if a and i:
    print('True3')
print(a and i)

# ---------------------------
# 블럭에 대한 정리
a = 10
if a:
    c = 2
elif i10:
    c = 5
else:
    c = 7
print(c)

#---------------
# find(): e단어를 찾으면 해당 인덱스 리턴하고 못찾음녀 -1리턴
word = 'korea'
print(word.find('k'))
for char in word:
    if char == 'k':
        print(word)

if word.find('k') > -1:
    print('1>' + word)

if word.find('z') > -1:
    print('2>' + word)