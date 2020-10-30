"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""


translate = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open('task4_eng.txt', 'r', encoding='UTF-8') as eng_file:
    with open('task4_rus.txt', 'w', encoding='UTF-8') as rus_file:
        for line in eng_file:
            f_data = line.split(' ')
            rus_file.write(f'{translate[int(f_data[2])]} {f_data[1]} {f_data[2]}')
