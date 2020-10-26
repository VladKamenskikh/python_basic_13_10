"""
Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка
в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""


def salary(output, rate, bonus):
    """ Функция расчета заработной платы сотрудника.
    Входные параметры: выработка в часах, ставка в час и премия.
    """
    result = output * rate + bonus
    return result


while True:
    try:
        output = float(input('Enter output in hours: '))
        rate = float(input('Enter rate: '))
        bonus = float(input('Enter bonus value: '))
        print(f'The salary is {salary(output, rate, bonus):.0f} dollars')
        break
    except ValueError:
        print('Incorrect enter. Try again.')
