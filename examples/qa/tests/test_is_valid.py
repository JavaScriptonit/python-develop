# Запуск тестов через командную строку
# `python3 -m unittest test_is_valid` - команда для запуска тестов из ./py-develop/examples/qa/tests

# Установка coverage:
# `pipenv install coverage`
# Запуск тестов через coverage (с созданием отчета):
# `pipenv run python3 -m coverage run -m unittest test_is_valid`
# `pipenv run python3 -m coverage report` - просмотр отчета
# Отчет (html):
# ./py-develop/examples/qa/tests/htmlcov/index.html

# Установка pytest:
# `pipenv install pytest`
# Запуск тестов через pytest:
# `pipenv run python3 -m pytest ./test_is_valid.py`
# Запуск тестов через pytest с coverage (с созданием отчета):
# `pipenv run python3 -m coverage run -m pytest ./test_is_valid.py`

import unittest

from is_valid import is_valid

class IsValidTestCase(unittest.TestCase):
    def test_is_valid(self):
        self.assertTrue(is_valid('()'))
        self.assertTrue(is_valid('[]'))
        self.assertTrue(is_valid('{}'))

    def test_is_not_valid(self):
        self.assertFalse(is_valid('('))
        self.assertFalse(is_valid('(}'))
        self.assertFalse(is_valid('({)}'))

# Asserts для pytest
def test_is_valid_pytest():
    assert is_valid('()')
    assert is_valid('[]')
    assert is_valid('{}')
    assert is_valid('(text) [C_123]()()() {} ({[]})')
    assert is_valid('({[(())]})')
    assert is_valid('(sdfds{[sdfsdfsd]})')

def test_is_not_valid_pytest():
    assert not is_valid('({[]}')
    assert not is_valid('(]')
    assert not is_valid('(')
    assert not is_valid('{{{{ ))))')
