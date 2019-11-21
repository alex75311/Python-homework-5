with open('example_task_3.txt', 'r', encoding='utf-8') as f:
    str_list = f.readlines()

sum_zp = 0
for idx, el in enumerate(str_list):
    el = el.split(':')
    lastname = el[0]
    zp = int(el[1].splitlines()[0])
    # print(lastname, zp)
    if zp < 20000:
        print(f'{lastname} получает меньше 20000')
    sum_zp += zp
print(f'Средняя зарплата составляет {sum_zp / len(str_list)}')
