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
