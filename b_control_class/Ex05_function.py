"""
    [ 함수 ]

     반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다

     def 함수명(매개변수):
        수행할 문장들
"""


# (1) 인자도 리턴값도 없는 함수
def func():
    print('함수 안에서 실행')
    return '결과값'


func()
print(func())  # 리턴값이 없으면 none


# (2) 리턴값이 여러개인 경우
def func(arg1, arg2):
    return arg1 + arg2, arg1 * arg2  # 리턴값이 여러개여도 된다


sum, multi = func(2, 3)
print('합:', sum, ' 곱:', multi)


# (3) 위치 인자 (positional argument)
def func(greeting, name):
    print(greeting, '!!!!', name, '님')
    

func('안녕', '박길동')
func('John', 'Hello')


# (4) 키워드 인자 (keyword argument)
func(name='울라프', greeting='올라')

# (5) 매개변수(인자)의 기본값 지정
def func(greeting='안녕', name='아무개'):
    print(greeting, '!!! ', name, '님')

func() # 위치인자의 갯수가 맞지 않아 에러
func(name='엘사') # 위치인자의 갯수가 맞지 않아 에러
func('올라', '울라프')


# [참고] 나중에 읽기
def buggy(arg, result=[]):
    result.append(arg)
    print(result)
    print(id(result)) # 주소 확인


buggy('가')  # ['가']
buggy('나')  # ['가', '나']
buggy('하', [1, 2, 3])  # [1, 2, 3, '하']
buggy('다')  # ['가', '나', '다']
'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (***********)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''


def func(a, b, c=0, *args):  # *args : 엄청 중요
    sum = a + b + c
    print(args)
    for i in args:
        sum += i
    print(sum)

print('====== positional argument ======')
func(4, 5)
func(4, 5, 6)
func(4, 5, 6, 7)
func(4, 5, 6, 7, 8, 9)


# *****************************
# (6) 키워드 인자 모으기 (keyword argument) : **kwargs
def func(a, b, c=0, **kwargs):
    sum = a + b + c
    for key in kwargs:
        sum += kwargs[key]
    print(sum)

print('====== keyword argument 모으기 ======')
func(4, 5)
func(4, 5, 6)
func(4, 5, 6, kor=7)
func(4, 5, 6, math=7, kor=8, java=9)