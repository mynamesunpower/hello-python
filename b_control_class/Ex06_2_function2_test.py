# 1
f = lambda x, y: x ** y

# 2
ex = [1, 2, 3, 4, 5]
square = lambda x: x ** 2
print(list(map(square, ex)))


# 3
def transpose_list(two_dimensional_list):
    return [row for row in zip(*two_dimensional_list)]


print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4
date_info = {'year': '2019', 'month': '9', 'day': '6'}
result = '{year}-{month}-{day}'.format(**date_info)
print(result)
# 2019-9-6

# 5


vector_size_check = lambda a, b, c: len(a) == len(b) == len(c)
a = (1, 2, 3)
b = (4, 5, 6)
c = (6, 7, 9)
print(vector_size_check(a, b, c))  # True

a = (1, 2, 3)
b = (4, 5, 6)
c = (6, 7)
print(vector_size_check(a, b, c))  # False

# 6

def matrix_addition(matrix1, matrix2):
    result = list(zip(matrix1, matrix2))
    print(result)


matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_addition(matrix_y, matrix_z)
