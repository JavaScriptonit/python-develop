# Функция для проверки корректности расстановки скобок
def is_valid(value: str) -> bool:
    stack = []  
    # Создаем пустой стек для хранения открывающих скобок
    brackets = {'(': ')', '[': ']', '{': '}'}
    # Словарь для соответствия открывающих и закрывающих скобок
    for ch in value:
        if ch in brackets.keys():  
            # Если текущий символ - открывающая скобка, добавляем ее в стек
            stack.append(ch)
        elif ch in brackets.values():  
            # Если текущий символ - закрывающая скобка
            if not stack or brackets[stack[-1]] != ch:  
                # Если стек пустой или последняя открывающая скобка не соответствует текущей закрывающей, возвращаем False
                return False
            stack.pop()  
            # Если соответствие найдено, удаляем соответствующую открывающую скобку из стека
    return len(stack) == 0  
    # Возвращаем True, если все открывающие скобки были правильно закрыты и стек пуст

# Проводим тестирование функции с различными входными данными
assert is_valid('()')
assert is_valid('[]')
assert is_valid('{}')
assert is_valid('(text) [C_123]()()() {} ({[]})')
assert is_valid('({[(())]})')
assert is_valid('(sdfds{[sdfsdfsd]})')

assert not is_valid('({[]}')
assert not is_valid('(]')
assert not is_valid('(')
assert not is_valid('{{{{ ))))')

print('SUCCESS!')
