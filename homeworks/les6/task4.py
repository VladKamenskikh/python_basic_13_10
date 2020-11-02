"""
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите
несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше
60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните
доступ к атрибутам, выведите результат. Выполните вызов методов и
также покажите результат.
"""


class Car:

    def __init__(self, speed: int, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print('Car goes.')

    def stop(self):
        if self.speed == 0:
            print('Car stops')

    def turn(self, direction):
        if self.speed > 0 and direction == 'right':
            print('Car turns right.')
        elif self.speed > 0 and direction == 'left':
            print('Car turns left.')
        else:
            Car.stop(self)

    def show_speed(self):
        print(f'Current speed is {self.speed}.')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("You're going too fast. Slow down.")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("You're going too fast. Slow down.")


class PoliceCar(Car):
    pass


vehicle = TownCar(65, 'Red', 'Cadillac', False)
vehicle.go()
vehicle.turn('right')
vehicle.show_speed()
