"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества
принтеров, отправленных на склад, нельзя использовать строковый тип
данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад
оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Warehouse:

    lst_of_equip = {}

    def send_from_wh(self):
        del self.lst_of_equip[OfficeEquipment(model_name='')]


class OfficeEquipment(Warehouse):

    def __init__(self, quantity, model_name, price):
        self.quantity = quantity
        self.model_name = model_name
        self.price = price

    def send_to_wh(self):
        if type(self.quantity) == int:
            Warehouse.lst_of_equip[self.model_name] = self.quantity
        else:
            print('Quantity must be integer!')


class Printer(OfficeEquipment):

    def __init__(self, type, color, format):
        super().__init__(OfficeEquipment)
        self.type = type
        self.color = color
        self.format = format


class Scanner(OfficeEquipment):

    def __init__(self, technology, resolution, bit_depth):
        super().__init__(OfficeEquipment)
        self.technology = technology
        self.resolution = resolution
        self.bit_depth = bit_depth


class Xerox(OfficeEquipment):

    def __init__(self, placement, power, memory):
        super().__init__(OfficeEquipment)
        self.placement = placement
        self.power = power
        self.memory = memory