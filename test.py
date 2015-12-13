import unittest

from unittest import TestCase

from calc import Calculator


class CalculatorTest(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(5.72, 3.8), 9.52)
        self.assertEqual(self.calculator.add(-3.2, 2.2), -1)
        self.assertEqual(self.calculator.add(3.2, -2.2), 1)
        self.assertEqual(self.calculator.add(-7.24, -6.5), -13.74)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertEqual(self.calculator.subtract(12.5, 5), 7.5)
        self.assertEqual(self.calculator.subtract(2, -6.17), 8.17)
        self.assertEqual(self.calculator.subtract(-5.5, 2), -7.5)
        self.assertEqual(self.calculator.subtract(-2.5, 3.5), -6)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5, 0), 0)
        self.assertEqual(self.calculator.multiply(3, 3), 9)
        self.assertEqual(self.calculator.multiply(3.27, -4.5), -14.715)
        self.assertEqual(self.calculator.multiply(-2.7, 4), -10.8)
        self.assertEqual(self.calculator.multiply(-6.2, -4), 24.8)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10.5, 2), 5.25)
        self.assertEqual(self.calculator.divide(-15.6, 3), -5.2)
        self.assertEqual(self.calculator.divide(-4.4, 4), -1.1)
        self.assertEqual(self.calculator.divide(-10, -5), 2)
        self.assertRaises(ValueError, lambda: self.calculator.divide(1, 0))

    def test_evaluate(self):
        self.assertEqual(self.calculator.evaluate('2+6-3'), 5)
        self.assertEqual(self.calculator.evaluate('6*8/4'), 12.0)
        self.assertEqual(self.calculator.evaluate('5+4*2'), 13.0)
        self.assertEqual(self.calculator.evaluate('6/3-2'), 0.0)
        self.assertRaises(SyntaxError, lambda: self.calculator.evaluate('(1+2*5'))
        self.assertRaises(ZeroDivisionError, lambda: self.calculator.evaluate('(4-2)/0'))

if __name__ == '__main__':
    unittest.main()
