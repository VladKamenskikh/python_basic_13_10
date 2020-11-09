"""
Продолжить работу над первым заданием. Разработать методы, отвечающие
за приём оргтехники на склад и передачу в определенное подразделение
компании. Для хранения данных о наименовании и количестве единиц
оргтехники, а также других данных, можно использовать любую подходящую
структуру, например словарь.
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
        Warehouse.lst_of_equip[self.model_name] = self.quantity


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


a = OfficeEquipment(5, 'Canon', 4000)
b = OfficeEquipment(7, 'HP', 6000)
a.send_to_wh()
b.send_to_wh()
print(Warehouse.lst_of_equip)