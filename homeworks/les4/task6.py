"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при
достижении числа 10 завершаем цикл. Во втором также необходимо
предусмотреть условие, при котором повторение элементов списка будет
прекращено.
"""
from itertools import (count,
                       cycle)


def number_generator(start, step, stop=10):
    """Функция генерирует целые числа начиная с указанного в start
    с шагом step. Для остановки генератора выставляется значение stop,
    по умолчанию равное 10.
    """
    result = count(start, step)
    counter = next(result)
    while counter < stop:
        print(counter, end=" ")
        counter = next(result)
    return counter


def word_generator(user_list, stop=20):
    """Функция повторяет элементы списка. В параметре stop указывается
    число повторений элементов, по умолчанию 20.
    """
    word_list = user_list.split()
    result = cycle(word_list)
    cycle_counter = next(result)
    k = 0
    while True:
        print(cycle_counter, end=" ")
        cycle_counter = next(result)
        k += 1
        if k == stop:
            break
    return cycle_counter
