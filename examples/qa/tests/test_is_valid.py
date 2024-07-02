import unittest

from is_valid import is_valid

class IsValidTestCase(unittest,TestCase):
    def test_is_valid(self):
        self.assertTrue(is_valid('()'))
        self.assertTrue(is_valid('[]'))
        self.assertTrue(is_valid('{}'))

    def test_is_not_valid(self):
        self.assertFalse(is_valid('('))
        self.assertFalse(is_valid('(}'))
        self.assertFalse(is_valid('({)}'))

