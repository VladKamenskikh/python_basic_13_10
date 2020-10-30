"""
Необходимо создать (не программно) текстовый файл, где
каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому
предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


k = 0
result = 0
result_list = []
result_dict = dict()
with open('task6_file.txt', 'r', encoding='UTF-8') as file:
    while True:
        for line in file.readlines():
            data = line.split(':')
            s = ''.join(i for i in line if i.isdigit() or i == ' ').strip().split(' ')
            for i in s:
                if i.isdigit():
                    result += int(i)
            result_list.append(result)
            result = 0
            result_dict[data[0]] = result_list[k]
            k += 1
        break
print(result_dict)
