"""
Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках
класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу
«Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.date = f'{day}-{month}-{year}'

    @classmethod
    def extractor(cls, date):
        day, month, year = date.split('-')
        day, month, year = int(day), int(month), int(year)
        return cls(day, month, year)

    @staticmethod
    def validator(month):
        if 1 <= month <= 12:
            return print('Your enter is correct!')
        else:
            return print('Month must be between 1 and 12!')


date1 = Date('07', '08', '1990')
new_date = date1.date
extr_date = Date.extractor(new_date)
valid = date1.validator(extr_date.month)
