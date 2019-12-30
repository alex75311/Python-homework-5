'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести
фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''

with open('example_task_3.txt', 'r', encoding='utf-8') as f:
    str_list = f.readlines()

sum_zp = 0
for idx, el in enumerate(str_list):
    el = el.split(':')
    last_name = el[0]
    zp = int(el[1].splitlines()[0])
    if zp < 20000:
        print(f'{last_name} получает меньше 20000')
    sum_zp += zp
print(f'Средняя зарплата составляет {sum_zp / len(str_list)}')
