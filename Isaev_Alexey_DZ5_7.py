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
