# 1
def check_bmi(height, weight):
    bmi = weight / ((height / 100) ** 2)
    if 20 <= bmi <= 24.9:
        print('정상입니다')
    elif 25 <= bmi <= 29.9:
        print('과체중입니다')
    elif 30 <= bmi:
        print('비만입니다')
    else:
        print('뭔가가 이상하다')


# check_bmi(float(input('신장을 입력하세요: ')), float(input('체중을 입력하세요: ')))

# 2
def lottery(number):
    import random
    lotto = str(random.randint(1, 99))
    if len(number) < 2:
        number = '0' + number
    if len(lotto) < 2:
        lotto = '0' + lotto
    print('number:', number, 'lotto:', lotto)
    result = 0
    for char in number:
        if lotto.count(char):
            result += 1
    print('result:', result)
    print('상금 100만원!' if result > 1 else '상금 50만원' if result > 0 else '상금은 없습니다')


# lottery(input('복권 번호(1-99사이)를 입력하시오: '))

# 3
def even_filter(arg_list):
    return [i for i in arg_list if i % 2 == 0]


# print(even_filter([1, 2, 4, 5, 8, 9, 10]))

# 4
def is_prime_number(number):
    result = 0
    for i in range(1, number + 1):
        if number % i == 0:
            result += 1

    return '소수가 아닙니다' if result > 2 else '소수입니다'


# print(is_prime_number(60))
# print(is_prime_number(61))

# 5
def count_vowel(word):
    result = 0
    for letter in set(word):
        if letter in ['a', 'e', 'i', 'o', 'u']:
            result += word.count(letter)

    return result


# print(count_vowel('pythonian'))
