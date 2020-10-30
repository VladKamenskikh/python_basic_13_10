"""
Создать (не программно) текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль
каждой компании, а также среднюю прибыль. Если фирма
получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с
фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000},
{"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

with open('task7_file.txt', 'r', encoding='UTF=8') as file:
    profit_sum = 0
    counter = 0
    profit = dict()
    for lines in file.readlines():
        profit_data = lines.split(' ')
        difference = int(profit_data[2]) - int(profit_data[3])
        profit[profit_data[0]] = difference
        if difference > 0:
            profit_sum += difference
            counter += 1
    result = [profit, {"average_profit": int(profit_sum / counter)}]
with open('task7_result.json', 'w', encoding='UTF=8') as json_file:
    json.dump(result, json_file)
