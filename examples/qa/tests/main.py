from is_valid import is_valid

file = open("text.txt")

print(f'Вывод информации о файле: {file}') # <_io.TextIOWrapper name='text.txt' mode='r' encoding='UTF-8'>

# print(f'Вывод результатов проверки кода в файле: {is_valid(file.read())}') # Вывод результатов проверки кода в файле

line_number = 0

for line in file.readlines():
    line_number += 1

    print(f'Строка № {line_number} из файла text.txt: {line}') # Вывод текста каждой строчки
    print(f'строка № {line_number} валидна: {is_valid(line)}') # Вывод результатов проверки кода на каждой строчке
    print(f'===================================================')

file.close()