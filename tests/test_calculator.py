import unittest
from app.calculator import Calculator
from app.operations import Addition, Subtraction, Multiplication, Division
from app.exceptions import CalculatorError, DivisionByZeroError

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.calculate(2, 3, Addition())
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calculator.calculate(5, 3, Subtraction())
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = self.calculator.calculate(4, 3, Multiplication())
        self.assertEqual(result, 12)

    def test_division(self):
        result = self.calculator.calculate(6, 2, Division())
        self.assertEqual(result, 3)

    def test_division_by_zero(self):
        with self.assertRaises(DivisionByZeroError):
            self.calculator.calculate(5, 0, Division())

if __name__ == '__main__':
    unittest.main()