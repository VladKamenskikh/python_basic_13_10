"""
Создайте собственный класс-исключение, обрабатывающий ситуацию
деления на нуль. Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться
с ошибкой.
"""


class ZeroDivError(Exception):

    def __init__(self, txt):
        self.txt = txt


f_number = int(input("Enter first number: "))
s_number = int(input("Enter second number: "))

try:
    if s_number == 0:
        raise ZeroDivError("Can't divide to zero!")
except ValueError:
    print('Enter single number without separators!')
except ZeroDivError as err:
    print(err)
else:
    print(f"Your number is: {f_number / s_number:.1f}")
