import unittest

from unittest import TestCase

from calculator import Calculator


class CalculatorTest(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(12, 5), 17)
        self.assertEqual(self.calculator.add(-2, 6), 4)
        self.assertEqual(self.calculator.add(5, -2), 3)
        self.assertEqual(self.calculator.add(-2, -3), -5)
        self.assertEqual(self.calculator.add(888888888888888888888888888888, 888888888888888888888888888888), 1777777777777777777777777777776)

        self.assertRaises(ValueError, lambda: self.calculator.add('qwe', 3))
        self.assertRaises(ValueError, lambda: self.calculator.add(1, 'qwe'))

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(-3, 2), -5)
        self.assertEqual(self.calculator.subtract(3, -2), 5)
        self.assertEqual(self.calculator.subtract(-7, -6), -1)
        self.assertEqual(self.calculator.subtract(-44444444444444444444444444444, -9999999999999999999999999999999999999999), 9999999999955555555555555555555555555555)

        self.assertRaises(ValueError, lambda: self.calculator.subtract('qwe', 3))
        self.assertRaises(ValueError, lambda: self.calculator.subtract(1, 'qwe'))


    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(0, 0), 0)
        self.assertEqual(self.calculator.multiply(3, 3), 9)
        self.assertEqual(self.calculator.multiply(-3, 4), -12)
        self.assertEqual(self.calculator.multiply(2, -4), -8)
        self.assertEqual(self.calculator.multiply(-6, -4), 24)
        self.assertEqual(self.calculator.multiply(888888888888888888888888888888, 44444444444444444), 39506172839506172444444444444404938271604938272)

        self.assertRaises(ValueError, lambda: self.calculator.multiply('qwe', 3))
        self.assertRaises(ValueError, lambda: self.calculator.multiply(1, 'qwe'))


    def test_divide(self):
        self.assertEqual(self.calculator.divide(0, 2), 0)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
        self.assertEqual(self.calculator.divide(-15, 3), -5)
        self.assertEqual(self.calculator.divide(4, -4), -1)
        self.assertEqual(self.calculator.divide(-10, -5), 2)
        self.assertEqual(self.calculator.divide(666666666666666666666666666666, 3333333333333333333), 200000000000)


        self.assertRaises(ValueError, lambda: self.calculator.divide(1, 0))
        self.assertRaises(ValueError, lambda: self.calculator.add('qwe', 3))
        self.assertRaises(ValueError, lambda: self.calculator.add(1, 'qwe'))

    def test_evaluate(self):
        self.assertEqual(self.calculator.evaluate('2+6-3'), 5)
        self.assertEqual(self.calculator.evaluate('6*8/4'), 12.0)
        self.assertEqual(self.calculator.evaluate('5+4*2'), 13.0)
        self.assertEqual(self.calculator.evaluate('6/3-2'), 0.0)

        self.assertRaises(SyntaxError, lambda: self.calculator.evaluate('(1+2*5'))
        self.assertRaises(ZeroDivisionError, lambda: self.calculator.evaluate('(4-2)/0'))
        #self.assertRaises(ValueError, lambda: self.calculator.evaluate('qwe'))

if __name__ == '__main__':
    unittest.main()
