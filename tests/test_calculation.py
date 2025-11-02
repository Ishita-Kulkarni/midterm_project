import unittest
from app.calculation import Calculation
from app.operations import Addition, Subtraction

class TestCalculation(unittest.TestCase):
    def test_calculation_execution(self):
        calc = Calculation(5, 3, Addition())
        self.assertEqual(calc.execute(), 8)

    def test_calculation_result_before_execution(self):
        calc = Calculation(5, 3, Addition())
        with self.assertRaises(ValueError):
            _ = calc.result

    def test_calculation_result_after_execution(self):
        calc = Calculation(5, 3, Subtraction())
        calc.execute()
        self.assertEqual(calc.result, 2)

if __name__ == '__main__':
    unittest.main()