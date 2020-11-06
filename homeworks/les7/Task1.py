"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные (список
списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода
матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый
элемент первой строки первой матрицы складываем с первым элементом
первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self):
        self.result = []
        counter = 0
        while True:
            arg = input('Enter 3 values with enter:').split(' ')
            arg = [int(el) for el in arg]
            self.result.append(arg)
            counter += 1
            if counter == 3:
                break

    def __str__(self):
        return f"{self.result[0]}\n{self.result[1]}\n{self.result[2]}"

    def __add__(self, other):
        result = []
        for el in self.result:
            for elem in other.result:
                result.append(list(map(sum, zip(el, elem))))
        return f"{result[0]}\n{result[4]}\n{result[-1]}"


mat1 = Matrix()
mat2 = Matrix()
print(mat1 + mat2)
