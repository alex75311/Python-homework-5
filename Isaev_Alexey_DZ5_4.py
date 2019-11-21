'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
'''

num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('example_task_4.txt', 'r', encoding='utf-8') as f:
    read_f = f.readlines()

for el in read_f:
    numeral = el.split()[0]
    el = el.replace(numeral, num_dict[numeral])
    with open('result_file_task_4.txt', 'a', encoding='utf-8') as f:
        print(''.join(el.splitlines()), file=f)
