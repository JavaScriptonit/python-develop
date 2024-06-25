# Урок - https://coursehunter.net/course/python-razrabotchik?lesson=8
# Документация - https://www.w3schools.com/python/python_lists_comprehension.asp

# Создаем список фруктов
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Используем генератор списка для создания нового списка newfruitslist, содержащего только те фрукты, в названии которых есть буква "a"
newfruitslist = [x for x in fruits if "a" in x]

# Выводим новый список фруктов, удовлетворяющих условию
print(newfruitslist)


# Создаем другой список фруктов
fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newfruits2list = []

# Используем цикл for для прохода по каждому элементу в списке fruits
for x in fruits2:
    # Проверяем, содержит ли название фрукта букву "a"
    if "a" in x:
        # Если содержит, добавляем этот фрукт в список newfruits2list
        newfruits2list.append(x)

# Выводим новый список фруктов, удовлетворяющих условию
print(newfruits2list)
