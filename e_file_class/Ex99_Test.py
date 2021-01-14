# 1
class Calculator:
    number_list = []

    def __init__(self, number_list):
        for number in number_list:
            self.number_list.append(number)

    def sum(self):
        result = 0
        for number in self.number_list:
            result += number
        return result

    def avg(self):
        return self.sum() / len(self.number_list)


cal = Calculator([1, 2, 3, 4, 5])
print(cal.sum())
print(cal.avg())


# 2
def calc_score():
    kor = int(input('국어점수를 입력->'))
    eng = int(input('영어점수를 입력->'))
    math = int(input('수학점수를 입력->'))
    print('총점:', kor+eng+math)
    print('평균: {:.2f}'.format((kor+eng+math)/3))

calc_score()

# 3
def multiply_vector(scalar=0, vector=None):
    if vector is None:
        vector = []
    print(list(map(lambda x: scalar * x, vector)))


multiply_vector(5, [1, 2, 3, 4])


# 4
def matrix_add(matrix_a=None, matrix_b=None):
    if matrix_a is None:
        matrix_a = [[], []]
    if matrix_b is None:
        matrix_b = [[], []]
    if len(matrix_a) != len(matrix_b):
        return '행렬의 크기가 일치하지 않습니다.'

    result = list()
    for i in range(len(matrix_a)):
        small_result = list()
        for j in range(len(matrix_a[i])):
            small_result.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(small_result)

    return result


matrix_x = [[2, 5], [2, 1]]
matrix_y = [[2, 4], [5, 3]]
print(matrix_add(matrix_x, matrix_y))


# 5
def vector_sub(vector=None):
    if vector is None:
        vector = [[]]

    result = []
    for i in range(2):
        value = vector[0][i]
        for j in range(1, len(vector)):
            value -= vector[j][i]
        result.append(value)

    return result


print(vector_sub([[1, 3], [2, 4]]))
print(vector_sub([[1, 5], [10, 4], [4, 7]]))

matrix_x = [[2, 5], [2, 1]]
matrix_y = [[2, 4], [5, 3]]


def matrix_add(matrix_x, matrix_y):
    result = [[sum(row_sum)for row_sum in zip(*x)] for x in zip(matrix_x, matrix_y)]
    #print(result)
    return matrix_add


print(matrix_add(matrix_x,matrix_y))