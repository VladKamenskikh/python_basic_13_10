"""
Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов. Определить, кто
из сотрудников имеет оклад менее 20 тыс., вывести фамилии
этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""


people = {}
summary = 0
value_counter = 0
with open('task3_file.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        key, value = line.split()
        people[key] = value
    for key, value in people.items():
        if int(value) < 20000:
            print(f'Guy with salary less than 20k is: {key}')
    for value in people.values():
        value_counter += 1
        summary += int(value)
        average = summary // value_counter
    print(f'Average salary is {average} dollars.')
