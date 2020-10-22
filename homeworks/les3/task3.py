"""
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func():
    """
    Функция принимает три позиционных аргумента и
    возвращает сумму наибольших двух.
    """
    while True:
        try:
            number1 = int(input('Enter first number: '))
            number2 = int(input('Enter second number: '))
            number3 = int(input('Enter third number: '))
            break
        except ValueError:
            print('You can do better!')
    my_f_list = [number1, number2, number3]
    k = 0
    for item in my_f_list:
        if my_f_list[k] < my_f_list[k+1] and my_f_list[k+1] < my_f_list[k+2]:
            result = my_f_list[k+1] + my_f_list[k+2]
        elif my_f_list[k] > my_f_list[k+1] and my_f_list[k+1] < my_f_list[2]:
            result = my_f_list[k] + my_f_list[k+2]
        else:
            result = my_f_list[k] + my_f_list[k+1]
    return result


print(f'Result: {my_func()}')
