import unittest
from calculation.tests.test_add import TestAdding
from calculation.tests.test_subtract import TestSubtract


def second_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestAdding('test_arguments_greater_zero'))
    suite.addTest(TestSubtract('test_arguments_greater_zero'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(second_suite())
