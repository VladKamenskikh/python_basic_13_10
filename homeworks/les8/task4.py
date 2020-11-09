"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
склад. А также класс «Оргтехника», который будет базовым для классов-
наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
ксерокс). В базовом классе определить параметры, общие для приведенных
типов. В классах-наследниках реализовать параметры, уникальные для каждого
типа оргтехники.
"""


class Warehouse:
    pass


class OfficeEquipment(Warehouse):

    def __init__(self, quantity, model_name, price):
        self.quantity = quantity
        self.model_name = model_name
        self.price = price


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
