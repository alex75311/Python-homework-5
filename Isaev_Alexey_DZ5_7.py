'''
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее ​ не включать​ .
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
© geekbrains.ru 24Пример json-объекта:
[{​ "firm_1"​ : ​ 5000​ , ​ "firm_2"​ : ​ 3000​ , ​ "firm_3"​ : ​ 1000​ }, {​ "average_profit"​ : ​ 2000​ }]
Подсказка: использовать менеджер контекста.
'''

import json

with open('example_task_7.txt', 'r', encoding='utf-8') as f:
    r_file = f.readlines()

res_dict = {}
average_dict = {}
pozitiv_profit = []
average_profit = 0
result = []

for el in r_file:
    name = ''.join(el.split()[:1])
    revenue = ''.join(el.split()[2:3])
    costs = ''.join(el.split()[-1:])
    profit = int(revenue) - int(costs)
    res_dict.update({name: profit})
    if profit >= 0:
        pozitiv_profit.append(profit)

for el in pozitiv_profit:
    average_profit += el
average_profit /= len(pozitiv_profit)

average_dict = {'average_profit': round(average_profit, 2)}
result.append(res_dict)
result.append(average_dict)
print(result)

with open('result_task_7.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)
