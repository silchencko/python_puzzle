import unittest
from unittest import TestCase
from calculation.calculation import subtract


class TestSubtract(TestCase):
    def test_arguments_greater_zero(self):
        num1 = 1
        num2 = 6
        result = subtract(num1, num2)
        # if the first argument is not 0, the result is not the second argument
        self.assertIsNot(result, num2)
        # if the second argument is not 0, the result is not the first argument
        self.assertIsNot(result, num1)

    def test_arguments_less_zero(self):
        num1 = -1
        num2 = -6
        result = subtract(num1, num2)
        # if the first argument is less then 0, the result is greater then it
        self.assertGreater(result, num1)
        # if the second argument is less then 0, the result is greater then it
        self.assertGreater(result, num2)

    def test_zero_argument(self):
        num1 = 0
        num2 = 6
        result = subtract(num1, num2)
        self.assertTrue(result == num1 or result == - num2)


if __name__ == '__main__':
    unittest.main()
