# Знакомство с Python и окружением для сборки:
1. `git --version` - вывести версию установленного гита:
    `git version 2.32.0 (Apple Git-132)`
2. `git config --local user.name Andrey` - устанавливает локальное имя пользователя (user.name) для репозитория Git
3. `git config --local user.email shabunovaa@yandex.ru` -  устанавливает локальный email пользователя (user.email) для репозитория Git
4. `python --version` - версия python:
    `Python 2.7.16`
5. `python ./main.py` - выполнение/запуск файла локально 
    `Hello world!`
6. `docker build -t python-develop:0.0.1 .` - сборка образа с созданным файлом и python:3
7. `docker run --rm python-develop:0.0.1` - выполнение/запуск контейнера с файлом локально


# Python console:
1. `python`: `>>>` - открытие консоли в терминале (можно использовать как калькулятор):
    1. `5 + 5` = `10`
    2. `2 ** 10` = `1024` - работа с числами
    3. `'Na ' * 16 + 'Batman'` = `'Na Na Na Na Na Na Na Na Na Na Na Na Na Na Na Na Batman'` - работать с текстовыми значениями
    4. `len(str(12313123123123123123))` = `20` - узнать длину числа в символах 


# Менеджмент зависимостей:
1. `pip` + `venv` = pip (менеджер зависимостей) + venv ("Virtualenv", создает изолированное окружение для проекта Python, не влияя на другие проекты)
2. `Pipenv` = более мощный аналог pip + venv
3. `Poetry` = не популярный аналог Pipenv
4. `Conda` = не популярный аналог Pipenv
5. `pipx` = не популярный аналог Pipenv

# Pipenv:
1. Менеджмент версий (Pipenv)
2. Менеджмент зависимостей (pip)
3. Виртуальные среды (venv)

