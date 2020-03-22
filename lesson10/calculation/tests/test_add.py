import unittest
from unittest import TestCase
from calculation.calculation import add


class TestAdding(TestCase):
    def test_arguments_greater_zero(self):
        num1 = 1
        num2 = 6
        result = add(num1, num2)
        self.assertGreater(result, num1)
        self.assertGreater(result, num2)

    def test_arguments_less_zero(self):
        num1 = -1
        num2 = -6
        result = add(num1, num2)
        self.assertLess(result, num1)
        self.assertLess(result, num2)

    def test_zero_argument(self):
        num1 = 0
        num2 = 6
        result = add(num1, num2)
        self.assertTrue(result == num1 or result == num2)


if __name__ == '__main__':
    unittest.main()
