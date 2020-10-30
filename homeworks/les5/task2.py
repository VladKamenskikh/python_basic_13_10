"""
Создать текстовый файл (не программно), сохранить в нем
несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


with open('task2_file.txt', 'r', encoding='UTF-8') as file:
    lines_counter = 0
    for lines in file:
        lines_counter += 1
        words_counter = len([itm for itm in lines.split() if itm != '' and itm != '\n'])
        print(f'In line {lines_counter} {words_counter} words.')
