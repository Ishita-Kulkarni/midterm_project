import unittest
from app.operations import Addition, Subtraction, Multiplication, Division

class TestOperations(unittest.TestCase):
    def test_addition(self):
        op = Addition()
        self.assertEqual(op.execute(2, 3), 5)
        self.assertEqual(op.symbol, '+')

    def test_subtraction(self):
        op = Subtraction()
        self.assertEqual(op.execute(5, 3), 2)
        self.assertEqual(op.symbol, '-')

    def test_multiplication(self):
        op = Multiplication()
        self.assertEqual(op.execute(4, 3), 12)
        self.assertEqual(op.symbol, '*')

    def test_division(self):
        op = Division()
        self.assertEqual(op.execute(6, 2), 3)
        self.assertEqual(op.symbol, '/')

if __name__ == '__main__':
    unittest.main()