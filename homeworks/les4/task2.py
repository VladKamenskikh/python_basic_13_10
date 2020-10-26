"""
Представлен список чисел. Необходимо вывести элементы
исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в
виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def comp_elem(user_list):
    """Функция преобразует введенный пользователем список и
    выводит элементы списка, значения которых больше предыдущего
    элемента.
    """
    transf_list = [int(i) for i in user_list if i.isdigit()]
    result_list = [transf_list[i+1] for i in range(len(transf_list)-1)
                   if transf_list[i+1] > transf_list[i]]
    return result_list


while True:
    try:
        user_list = input('Enter list of numbers: ').split()
        for itm in user_list:
            if itm.isdigit():
                print(f'Computed list: {comp_elem(user_list)}')
                break
        break
    except ValueError:
        print('Incorrect enter. Try again')
