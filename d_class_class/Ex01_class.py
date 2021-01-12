"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""


class Sample:
    data = 'hello'  # 멤버 변수 선언

    # 생성자 역할
    def __init__(self):
        self.age = 25  # 멤버 변수 선언
        self.name = '홍길동'
        print('__init__')

    # 소멸자 역할
    def __del__(self):
        print('__del__')


s = Sample()
print(s.data)
print(s.age)
print(s.name)
del s
print('프로그램 종료')

"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 
    하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    
    클래스   함수 :  'cls'인 클래스를 인자로 받고 
    모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
    
    [ 참고 ] static 함수 없어진 듯 (에러 남)
"""


class Book:
    cnt = 0

    def __init__(self, title):
        self.title = title  # 함수의 매개변수는 지역 변수지만 멤버변수로 지정하고 싶다면 ?

    # 인스턴스 함수 : 클래스 안에 있는 일반적인 함수
    def output(self):
        print('제목:', self.title)
        self.cnt += 1
        print('갯수:', self.cnt)

    # [소개] 클래스 함수
    @classmethod
    def output2(cls, title):
        # print('제목:', cls.title) self를 통해서 만들었기 때문에 self로만 접근 가능.
        print('제목:', title)
        cls.cnt += 1
        print('갯수:', cls.cnt) # 그냥 만들었기 때문에 cls, self 접근 가능

b1 = Book('정의란')
b2 = Book('다이어트란')
b1.output2(b1.title)
b2.output2(b2.title)

'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''
class Animal:

    def __init__(self):
        print('동물 생성')

    def move(self):
        print('동물은 움직인다')

class Wolf(Animal):  #  늑대는 동물을 상속한다
    def move(self):
        print('늑대는 4발로 달린다')

w = Wolf()
w.move()

class Human(Animal):
    def move(self):
        print('사람은 두 발로 걷는다')

h = Human()
h.move()

class Werewolf(Wolf, Human):
    def move(self):
        print('늑대인간은 두 발로 달린다')
        super().move()

ww = Werewolf()
ww.move()