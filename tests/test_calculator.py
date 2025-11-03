import unittest
from app.calculator import Calculator
from app.operations import Addition, Subtraction, Multiplication, Division
from app.exceptions import DivisionByZeroError

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Create a Calculator instance for each test."""
        self.calc = Calculator()

    def test_addition(self):
        result = self.calc.calculate(2, 3, Addition())
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calc.calculate(5, 3, Subtraction())
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = self.calc.calculate(4, 3, Multiplication())
        self.assertEqual(result, 12)

    def test_division(self):
        result = self.calc.calculate(10, 2, Division())
        self.assertEqual(result, 5)

    def test_division_by_zero_raises(self):
        with self.assertRaises(DivisionByZeroError):
            self.calc.calculate(5, 0, Division())

    def test_history_tracking(self):
        # Initially history should be empty
        self.assertEqual(len(self.calc.history), 0)

        # Perform a calculation and check history
        self.calc.calculate(2, 3, Addition())
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0].execute(), 5)

    def test_multiple_history_entries(self):
        self.calc.calculate(2, 3, Addition())
        self.calc.calculate(5, 2, Subtraction())
        self.assertEqual(len(self.calc.history), 2)
        self.assertEqual(self.calc.history[0].execute(), 5)
        self.assertEqual(self.calc.history[1].execute(), 3)

if __name__ == "__main__":
    unittest.main()
