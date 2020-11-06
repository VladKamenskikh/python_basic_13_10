"""
Реализовать проект расчета суммарного расхода ткани на производство
одежды. Основная сущность (класс) этого проекта — одежда, которая
может иметь определенное название. К типам одежды в этом проекте
относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные
числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике
полученные на этом уроке знания: реализовать абстрактные классы
для основных классов проекта, проверить на практике работу
декоратора @property.
"""


class Clothes:

    total = []

    def total_consumption(self):
        return f'Total consumption: {sum(self.total):.1f}'


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def coat_consumption(self):
        result = float(self.size / 6.5 + 0.5)
        super().total.append(result)
        return f'Coat fabric consumption: {result:.1f}'


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def suit_consumption(self):
        result = float(2 * self.height + 0.3)
        super().total.append(result)
        return f'Suit fabric consumption: {result:.1f}'


coat_obj = Coat(6)
coat_obj.coat_consumption
suit_obj = Suit(3)
suit_obj.suit_consumption
clothes_obj = Clothes()
print(clothes_obj.total_consumption())
