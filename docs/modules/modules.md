https://coursehunter.net/course/python-razrabotchik?lesson=7

# Модули в Python

Модули в Python - это файлы, содержащие Python код, который можно использовать в других программах. Они позволяют легко организовывать и переиспользовать код. 

- **Стандартные модули**: Предварительно установленный набор модулей, таких как `math`, `random`, `datetime`, которые широко используются для различных задач.
- **Сторонние модули**: Созданные сторонними разработчиками и доступные через инструменты управления пакетами, такие как `pip`.

#### Использование модулей
```python
import math
print(math.sqrt(16))  # Использование функции sqrt из модуля math

from random import randint
print(randint(1, 10))  # Импорт конкретной функции randint из модуля random
```

#### Создание собственных модулей
- Создайте файл с расширением `.py` и определите в нем функции, классы или переменные.
- Для использования своего модуля в другом файле импортируйте его с помощью `import`.

Модули - мощный инструмент для структурирования кода и повторного использования функциональности в Python.