# 1 프린트
pin = '880122-1234567'
birthday = '홍길동님 생년월일 : ' + pin[:6]
gender = '성별 : ' + '남자' if pin[7] == '1' or '3' else '여자'
print(birthday)
print(gender)

# 2 리스트 [1,3,5,4,2] 값을 [5,4,3,2,1]로 만들어서 출력한다.
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 3 리스트를 문자열로 만들어서 출력한다
a = ['독도는', '대한민국의', '아름다운', '섬입니다']
result = ' '.join(a)
print(result)

# 4 튜플 (1,2,3)에 4 값을 추가하여 (1,2,3,4)를 만들어 출력한다
a = (1, 2, 3)
a += (4,)
print(a)

# 5 아래 파이썬의 실행 결과를 확인하고 이런 결과가 나오는 이유에 대해 설명한다
a = b = [1, 2, 3]
a[1] = 4
print(b)  # [1, 4, 3] 얕은 복사이기 때문에 a와 b는 객체를 동일한 주소를 가리키고 있다. 그렇기에 [1, 2, 3] 리스트 객체의 값을 변경해도 a와 b의 결과가 같아진다.

# 6 별 찍기
print('\n'.join('*' * i for i in range(1, 6)))

# 7 애들 총점 찍기.
kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50, 60, 70, 80, 90]
midterm_score = [kor_score, math_score, eng_score]

from functools import reduce
def sum(x, y):
    return x + y

print('국어 점수 총점: {}, 평균: {}'.format(reduce(sum, kor_score), reduce(sum, kor_score) / len(kor_score)))
print('수학 점수 총점: {}, 평균: {}'.format(reduce(sum, math_score), reduce(sum, math_score) / len(math_score)))
print('영어 점수 총점: {}, 평균: {}'.format(reduce(sum, eng_score), reduce(sum, eng_score) / len(eng_score)))
for i, (kor, math, eng) in list(enumerate(zip(kor_score, math_score, eng_score))):
    print('{}번째 학생의 총점: {}, 평균: {:.2f}'.format(i + 1, kor + math + eng, (kor+math+eng)/3))

# 8 딕셔너리
life = dict()
for i in ['animal', 'plants', 'other']:
    life[i] = dict()
for i in ['cats', 'octopi', 'emus']:
    life['animal'][i] = dict()
for i in ['Kim', 'Lee', 'Choi']:
    life['animal']['cats'][i] = dict()