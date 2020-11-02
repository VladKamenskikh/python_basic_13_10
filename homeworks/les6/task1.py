"""
Создать класс TrafficLight (светофор) и определить у него один
атрибут color (цвет) и метод running (запуск). Атрибут реализовать
как приватный. В рамках метода реализовать переключение светофора
в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами
должно осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав
описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при
его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep


class TrafficLight:

    def __init__(self, __color='Red'):
        self.__color = __color

    def running(self):
        while True:
            self.__color = 'Red'
            print(f'Current color is {self.__color}')
            sleep(7)
            self.__color = 'Yellow'
            print(f'Current color is {self.__color}')
            sleep(2)
            self.__color = 'Green'
            print(f'Current color is {self.__color}')
            sleep(6)


Traffic_Light = TrafficLight()
Traffic_Light.running()
print(Traffic_Light.running())
