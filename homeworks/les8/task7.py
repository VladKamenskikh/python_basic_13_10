"""
Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:

    def __init__(self, number):
        self.number = complex(number)

    def __mul__(self, other):
        return self.number * complex(other.number)

    def __add__(self, other):
        return self.number + complex(other.number)


number1 = ComplexNumber(2)
number2 = ComplexNumber(4)
print(number1 * number2)
print(number1 + number2)
