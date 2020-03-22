import unittest
from calculation.tests.test_add import TestAdding
from calculation.tests.test_subtract import TestSubtract


def first_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestAdding('test_zero_argument'))
    suite.addTest(TestSubtract('test_zero_argument'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(first_suite())
