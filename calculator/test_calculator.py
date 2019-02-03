import unittest
import io
from calculator import Calculator
from unittest import mock
from unittest.mock import patch

class TestMyCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    def test_add(self):
        self.calc.add(1,3)
        self.assertEqual(4, self.calc.value)

    def test_substract(self):
        self.calc.substract(2, 2)
        self.assertEqual(0, self.calc.value)

    def test_multiply(self):
        self.calc.multiply(2,3)
        self.assertEqual(6, self.calc.value)

    def test_divide(self):
        self.calc.divide(6,2)
        self.assertEqual(3, self.calc.value)

    # Solution: testing print with @patch
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_divide_zero(self, mock_stdout):
        self.calc.divide(3,0)
        self.assertEqual(mock_stdout.getvalue(), 'You can\'t divide by zero!\n')


if __name__ == '__main__':
    unittest.main()
