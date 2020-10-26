"""
Реализовать генератор с помощью функции с ключевым словом
yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна
вызываться следующим образом: for el in fact(n). Функция
отвечает за получение факториала числа, а в цикле необходимо
выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fact(n):
    """Функция находит факториал числа n.
    """
    start = 1
    result = 1
    while start <= n:
        result *= start
        yield result
        start += 1


while True:
    try:
        user_data = int(input('Enter number for factorial: '))
        if user_data <= 0:
            print('Number must be positive!')
            continue
        final = [el for el in fact(user_data)]
        print(f'Result: {final}')
        break
    except ValueError:
        print('Incorrect enter. It must be number!')
