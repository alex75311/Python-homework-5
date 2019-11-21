num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('example_task_4.txt', 'r', encoding='utf-8') as f:
    read_f = f.readlines()

for el in read_f:
    numeral = el.split()[0]
    el = el.replace(numeral, num_dict[numeral])
    with open('result_file_task_4.txt', 'a', encoding='utf-8') as f:
        print(''.join(el.splitlines()), file=f)
