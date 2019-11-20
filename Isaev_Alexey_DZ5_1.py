with open('input_text.txt', 'w') as f:
    while True:
        usr_str = input('Введите строку для записи в файл\n')
        if usr_str:
            f.write(usr_str + '\n')
        else:
            break
