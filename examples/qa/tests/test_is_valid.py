# Запуск тестов через командную строку
# `python3 -m unittest test_is_valid` - команда для запуска тестов из ./py-develop/examples/qa/tests

# Установка coverage:
# `pipenv install coverage`
# Запуск тестов через coverage с созданием отчета:
# `pipenv run python3 -m coverage run -m unittest test_is_valid`
# `pipenv run python3 -m coverage report` - просмотр отчета
# Отчет (html):
# ./py-develop/examples/qa/tests/htmlcov/index.html

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
