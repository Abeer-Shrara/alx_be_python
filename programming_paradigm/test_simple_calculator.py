# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a calculator instance before each test runs."""
        self.calc = SimpleCalculator()

    # ---- Addition Tests ----
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)         # normal case
        self.assertEqual(self.calc.add(-1, 1), 0)        # negative + positive
        self.assertEqual(self.calc.add(-2, -3), -5)      # negative + negative
        self.assertEqual(self.calc.add(0, 5), 5)         # adding zero
        self.assertEqual(self.calc.add(2.5, 0.5), 3.0)   # decimals

    # ---- Subtraction Tests ----
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)    # normal case
        self.assertEqual(self.calc.subtract(0, 5), -5)   # subtract larger from smaller
        self.assertEqual(self.calc.subtract(-5, -3), -2) # negative - negative
        self.assertEqual(self.calc.subtract(5, 0), 5)    # subtracting zero
        self.assertEqual(self.calc.subtract(2.5, 0.5), 2.0)  # decimals

    # ---- Multiplication Tests ----
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)    # normal case
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # negative * positive
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # negative * negative
        self.assertEqual(self.calc.multiply(5, 0), 0)    # multiplying by zero
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0) # decimals

    # ---- Division Tests ----
    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2.0)    # normal case
        self.assertEqual(self.calc.divide(-6, 3), -2.0)  # negative / positive
        self.assertEqual(self.calc.divide(-6, -3), 2.0)  # negative / negative
        self.assertEqual(self.calc.divide(5, 2), 2.5)    # division with remainder
        self.assertIsNone(self.calc.divide(5, 0))        # division by zero returns None


if __name__ == "__main__":
    unittest.main()
