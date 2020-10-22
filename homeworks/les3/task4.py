"""
Программа принимает действительное положительное число x и
целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.
"""


def expon():
    """
    Функция принимает действительное положительное число x,
    целое отрицательное число y, возводит x в степень y с
    помощью встроенной функции возведения числа в степень.
    """
    while True:
        try:
            x = float(input('Enter positive float number: '))
            y = int(input('Enter negative int number: '))
            if x > 0 and y < 0:
                break
            else:
                print('Numbers are incorrect!')
        except ValueError:
            print('Try again')
    result = x ** y
    return result


def expon2():
    """
    Функция принимает действительное положительное число x,
    целое отрицательное число y, возводит x в степень y с
    помощью цикла.
    """
    while True:
        try:
            x = float(input('Enter positive float number: '))
            y = int(input('Enter negative number: '))
            if x > 0 and y < 0:
                break
            else:
                print('Numbers are incorrect!')
        except ValueError:
            print('Try again')
    k = 0
    sum = 1
    while k < abs(y):
        sum *= x
        k += 1
    result = 1 / sum
    return result


print(f'Result: {expon()}')
print(f'Result: {expon2()}')
