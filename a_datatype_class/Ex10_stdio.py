"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""

# -------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
# age = int(input('나이 입력 -> '))
# print(type(age))
# print(age+1, '세입니다')
# height = float(input('키 입력 -> '))
# print(type(height))
# print(height, 'cm입니다')


# ----------------------------------
# 단을 입력받아 구구단을 구하기
num = int(input('단 입력-> '))
for i in range(1, 10):
    print('{} * {} = {} '.format(num, i, num*i))

# -----------------------------------------
# print() 함수
print('안녕'+'친구')  # 안녕친구
print('안녕', '친구')  # 안녕 친구
print('안녕' '친구')  # 안녕친구
for i in range(2, 8):
    print(i, end=', ' if i < 7 else "") # 옵션이 없으면 자동 개행
print('----------------------')

print(','.join(str(i) for i in range(2, 8)))

# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3
import sys
args = sys.argv[1:]
for i in args:
    print(i)
print('서버 연결')

# 1
a = []
for i in range(5):
    a.append(int(input('정수를입력하세요: ')))
sum = 0
for i in a:
    sum += i
print('평균=',sum/len(a))

# 2
b = str(input('문자열입력: '))
print(b[::-1])

# 3
integer_list = input('정수리스트입력: ').split()
sum = 0
for number in integer_list:
    sum += int(number)
average = sum / len(integer_list)
print('평균: {:.1f}'.format(average))
deviation_sum = 0
for number in integer_list:
    deviation = int(number) - average
    deviation_sum += deviation ** 2
variance = deviation_sum / len(integer_list)
print('분산: {:.1f}'.format(variance))
print('표준편차: {:.2f}'.format(variance ** (1/2)))

# 4
phone = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],
         ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],
         ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
string = input('문자열을입력하시오: ')
result = ''
for char in string:
    for i in range(len(phone)):
        if char.upper() in phone[i]:
            result += str(i + 1)
print(result)
