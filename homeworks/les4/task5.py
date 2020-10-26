"""
Реализовать формирование списка, используя функцию
range() и возможности генератора. В список должны
войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения
всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

result_list = [itm for itm in range(100, 1001) if itm % 2 == 0]
result = reduce(lambda x, y: x*y, result_list)
print(f'Result: {result}')
