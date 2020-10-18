"""
Реализовать структуру данных «Товары». Она должна представлять
собой список кортежей. Каждый кортеж хранит информацию об
отдельном товаре. В кортеже должно быть два элемента — номер
товара и словарь с параметрами (характеристиками товара:
название, цена, количество, единица измерения). Структуру нужно
сформировать программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в
котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список
названий товаров.
"""
item_param = dict()
item_param2 = dict()
item_param3 = dict()
items = (1, item_param)
item_param['Name'] = input('Enter item name: ')
item_param['Price'] = int(input('Enter price: '))
item_param['Quantity'] = int(input('Enter quantity: '))
item_param['Unit'] = input('Enter units: ')
items2 = (2, item_param2)
item_param2['Name'] = input('Enter item name: ')
item_param2['Price'] = int(input('Enter price: '))
item_param2['Quantity'] = int(input('Enter quantity: '))
item_param2['Unit'] = input('Enter units: ')
items3 = (3, item_param3)
item_param3['Name'] = input('Enter item name: ')
item_param3['Price'] = int(input('Enter price: '))
item_param3['Quantity'] = int(input('Enter quantity: '))
item_param3['Unit'] = input('Enter units: ')
item_sort = dict()
item_sort['Name'] = [item_param.get('Name'), item_param2.get('Name'), item_param3.get('Name')]
item_sort['Price'] = [item_param.get('Price'), item_param2.get('Price'), item_param3.get('Price')]
item_sort['Quantity'] = [item_param.get('Quantity'), item_param2.get('Quantity'), item_param3.get('Quantity')]
item_sort['Unit'] = [item_param.get('Unit'), item_param2.get('Unit'), item_param3.get('Unit')]
print(items)
print(items2)
print(items3)
print(item_sort)