# Урок - https://coursehunter.net/course/python-razrabotchik?lesson=8
# Создаем список
from ast import NotIn


my_list = [2, 7, 5, 10, 15, 3, 8, 6, 9, 4]

# Проверяем наличие цифры 5 в списке
if 5 in my_list:
    print("Цифра 5 найдена в списке.")
else:
    print("Цифра 5 не найдена в списке.")

# Проверяем отсутствие цифры 22 в списке
if 22 not in my_list:
    print("Цифра 22 не найдена в списке.")
else:
    print("Цифра 22 найдена в списке.")
