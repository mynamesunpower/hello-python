"""
    sum 함수 정의하기
    - 2개의 인자를 받아 더한 값을 리턴한다
    - 그러나 다른 자료형이면 자료형이 달라서 계산할 수 없습니다라고 출력
"""


def deohagi(x, y):
    if type(x) != type(y):
        return '자료형이 달라서 계산할 수 없습니다.'
    else:
        return x + y


deohagi2 = lambda x, y: '자료형이 달라서 계산할 수 없습니다' if type(x) != type(y) else x + y


# --------------------
# 파이썬 함수 역할
if __name__ == '__main__':  # 프로그램 시작점
    print(deohagi2(2, 3))
    print(deohagi2('hello', 'jack'))
    print(deohagi2(500, 'jack'))