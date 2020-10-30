"""
Создать (программно) текстовый файл, записать в него
программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


sum = 0
with open('task5_file.txt', 'w', encoding='UTF-8') as file:
    print('1 3 5 4 9 3 2 8 1 9 5 11 13\n', file=file)
with open('task5_file.txt', 'r', encoding='UTF-8') as file:
    numbers = file.read().split(' ')
    for itm in numbers:
        itm = int(itm)
        sum += itm
    print(f'Sum of numbers in file is {sum}.')
