'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30 (л) ​ —​ 10 (лаб)
Физкультура: ​ — 30 (пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

with open('example_task_6.txt', 'r', encoding='utf-8') as f:
    r_file = f.readlines()

arr = {}
for el in r_file:
    training = ''.join(el.split()[:1])[:-1]
    oth = el.split()[1:]
    summa = 0
    for el in oth:
        if el.isdigit():
            summa += int(el)
    arr.update({training: summa})

print(arr)
