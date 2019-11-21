with open('example_task_5.txt', 'w', encoding='utf-8') as f:
    f.write('20 21 22 23 24 25 26 27 28 29 30')

with open('example_task_5.txt', 'r', encoding='utf-8') as f:
    read_file = f.readline().split()

summ = 0
for el in read_file:
    summ += int(el)
print(f'Сумма чисел в файле равна {summ}')
