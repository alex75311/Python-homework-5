'''
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

file_name = 'input_text.txt'
with open(file_name, 'w', encoding='utf-8') as f:
    while True:
        usr_str = input('Введите строку для записи в файл (для окончания ввода введите пустую строку)\n')
        if usr_str:
            f.write(usr_str + '\n')
        else:
            print(f'Файл {file_name} сохранен')
            break
