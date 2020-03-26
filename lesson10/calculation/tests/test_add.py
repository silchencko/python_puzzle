import unittest
from unittest import TestCase
from calculation.calculation import add


class TestAdding(TestCase):
    def test_arguments_greater_zero(self):
        num1 = 1
        num2 = 6
        result = add(num1, num2)
        self.assertEqual(result, 7)

    def test_arguments_less_zero(self):
        num1 = -1
        num2 = -6
        result = add(num1, num2)
        self.assertLess(result, num1)
        self.assertLess(result, num2)

    def test_first_zero_argument(self):
        num1 = 0
        num2 = 6
        result = add(num1, num2)
        self.assertTrue(result == num2)

    def test_second_zero_argument(self):
        num1 = 6
        num2 = 0
        result = add(num1, num2)
        self.assertTrue(result == num1)


if __name__ == '__main__':
    unittest.main()
