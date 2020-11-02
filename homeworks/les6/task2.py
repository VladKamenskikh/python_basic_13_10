"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать
защищенными. Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна. Использовать формулу: длина *
ширина * масса асфальта для покрытия одного кв метра дороги
асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить
работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_volume(self, volume_for_1m, thickness):
        volume = self._length * self._width * volume_for_1m * thickness
        print(f'Volume needed for asphalt coverage is {volume/1000:.0f} t')


RoadCover = Road(20, 5000)
RoadCover.asphalt_volume(25, 5)
