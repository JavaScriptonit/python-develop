# Знакомство с Python и окружением для сборки:
1. `git --version` - вывести версию установленного гита:
    `git version 2.32.0 (Apple Git-132)`
2. `git config --local user.name Andrey` - устанавливает локальное имя пользователя (user.name) для репозитория Git
3. `git config --local user.email shabunovaa@yandex.ru` -  устанавливает локальный email пользователя (user.email) для репозитория Git
4. Версии python на macOS:
    1. `python --version` - версия python: `Python 2.7.16`
    2. `python3 --version` - `Python 3.11.1`
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

# Запуск игры локально:
1. `git clone https://github.com/eldop/Jerry-s-Game.git` - скачать игру

## С помощью venv (КЛАССИЧЕСКИЙ подход):
1. `python3 -m venv env` - создать вирт окружение для переменных проекта
2. `source env/bin/activate` - активация виртуальной среды в проекте на macOS
    1. `deactivate` - выключение вирт среды
3. `pip install pygame` - скачать единственную зависимость для проекта в вирт среде (env): `Successfully installed pygame-2.5.2`
4. `python ./main.py` - запуск игры

## С помощью Pipenv (ПРОФЕССИОНАЛЬНЫЙ подход):
1. `pip install pipenv` - установка Pipenv: `Successfully installed distlib-0.3.8 filelock-3.15.1 pipenv-2024.0.1 platformdirs-4.2.2 setuptools-70.0.0 virtualenv-20.26.2`
2. `pipenv shell` - устанавливается вирт окружение: `✔ Successfully created virtual environment!`:
    1. `Virtualenv location: /Users/andreyshabunov/.local/share/virtualenvs/Jerry-s-Game-zutpkkIc` - хранилище
3. `pipenv install pygame` - скачать зависимость для проекта & создать Pipfile.lock файл с версий зависимости
4. `pipenv run python3 ./main.py` - запуск игры
