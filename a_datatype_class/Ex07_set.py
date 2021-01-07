# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다


s = set()               # 빈 집합을 생성
s = set([1,2,3,1,1])
print(s)
s2 = {3, 4, 5}
s3 = {2, 3, 7, 1, 1}
print(s2)
print(s3)
print(type(s))
print(type(s2))
print(type(s3))

print(s.intersection(s2))
print(s & s2)

print(s.union(s2))
print(s | s2)

print(s.difference(s2))
print(s - s2)

# 참고
# -- 정수인 경우 0 - false, 0이 아니면 True
a = 10
b = -1
if a and b:
    print('True1')
if a or b:
    print('True2')
print(a and b)
print(a or b)

print(s and s2) # s2 가 나오넹
print(s or s2) # s 가 나오넹

if a:
    print(a)