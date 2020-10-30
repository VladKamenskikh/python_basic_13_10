"""
Создать программно файл в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода
данных свидетельствует пустая строка.
"""


with open('task1_file.txt', 'w', encoding='UTF-8') as file:
    user_data = input('Enter text line: ')
    while user_data != '':
        file.write(user_data + '\n')
        user_data = input('Enter text line: ')
