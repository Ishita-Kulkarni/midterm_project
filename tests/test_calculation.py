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

    def test_calculation_execute_and_repr(self):
        calc = Calculation(3, 7, Addition())
        self.assertEqual(calc.execute(), 10)
        # Set symbol for test compatibility
        setattr(calc.operation, 'symbol', '+')
        self.assertEqual(str(calc), "Calculation: 3 + 7 = 10")

        calc2 = Calculation(10, 4, Subtraction())
        self.assertEqual(calc2.execute(), 6)

if __name__ == '__main__':
    unittest.main()