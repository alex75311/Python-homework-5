'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
'''

with open('input_text.txt', 'r', encoding='utf-8') as f:
    str_list = f.readlines()

print(f'Кол-во строк в этом файле {len(str_list)}')
for idx, el in enumerate(str_list):
    print(f'Строка {idx + 1}: {el.splitlines()}')
    print(f'Количество слов в {idx + 1} строке: {len(el.split())}')
