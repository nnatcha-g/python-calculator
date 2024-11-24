import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_negative_and_positive(self):
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    def test_divide_by_one(self):
        self.assertEqual(self.calc.divide(10, 1), 10)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_modulo_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(10, 0)

    def test_modulo_negative_numbers(self):
        self.assertEqual(self.calc.modulo(-10, 3), 2)

if __name__ == '__main__':
    unittest.main()