import unittest
from unittest_prettify.colorize import *
from calculator.arithmetic.advanced import Advanced
from calculator.arithmetic.exceptions import BadOperandException


@colorize(color=RED)
class PowerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.op = Advanced()
    def test_square(self):
        """Basic power of 2"""
        base = 5
        exp = 2
        self.assertEqual(25, self.op.power(base, exp))

    def test_exp(self):
        """Basic exponent"""
        base = 2
        exp = 10
        self.assertEqual(1024, self.op.power(base, exp))

    def test_negative_exp(self):
        """Negative exponent"""
        base = 5
        exp = -3
        self.assertEqual(1/125, self.op.power(base, exp))

    def test_negative_base(self):
        """Negative base"""
        base = -4
        exp = 3
        self.assertEqual(-64, self.op.power(base, exp))

    def test_both_negative(self):
        """Both base and exp are negative"""
        base = -5
        exp = -2
        self.assertEqual(1/25, self.op.power(base, exp))

    def test_float(self):
        """Float base"""
        base = 6.74
        exp = 4
        self.assertEqual(2063.6668418, self.op.power(base, exp))

    def test_bigger_num(self):
        """Some bigger number"""
        base = 10
        exp = 10
        self.assertEqual(10000000000, self.op.power(base, exp))


@colorize(color=GREEN)
class FactorialTests(unittest.TestCase):

    def setUp(self) -> None:
        self.op = Advanced()

    def test_basic(self):
        """Basic factorial"""
        num = 3
        self.assertEqual(6, self.op.factorial(num))

    def test_zero(self):
        """Zero factorial"""
        num = 0
        self.assertEqual(1, self.op.factorial(num))

    def test_negative(self):
        """Negative argument"""
        num = -5
        self.assertRaises(BadOperandException, self.op.factorial, num)

    def test_bigger(self):
        """Some mid number"""
        num = 10
        self.assertEqual(3628800, self.op.factorial(num))

    def test_float(self):
        """Float number"""
        num = 3.3
        self.assertRaises(BadOperandException, self.op.factorial, num)

    def test_negative_num_exception(self):
        """Negative number"""
        num = -10
        self.assertRaises(BadOperandException, self.op.factorial, num)


@colorize(color=YELLOW)
class LogarithmTests(unittest.TestCase):

    def setUp(self) -> None:
        self.op = Advanced()

    def test_basic(self):
        """Basic test"""
        base = 2
        num = 8
        self.assertEqual(3, self.op.logarithm(num, base))

    def test_negative_base(self):
        """Negative base"""
        base = -2
        num = 8
        self.assertRaises(BadOperandException, self.op.logarithm, num, base)

    def test_negative_num(self):
        """Negative log body"""
        base = 3
        num = -27
        self.assertRaises(BadOperandException, self.op.logarithm, num, base)

    def test_both_negative(self):
        """Negative both base and number"""
        base = -3
        num = -10
        self.assertRaises(BadOperandException, self.op.logarithm, num, base)

    def test_float_result(self):
        base = 2
        num = 15
        self.assertEqual(3.9068906, self.op.logarithm(num, base))

    def test_negative_num_exception(self):
        """Negative number"""
        base = 2
        num = -32
        self.assertRaises(BadOperandException, self.op.logarithm, num, base)

    def test_negative_base_exception(self):
        """Negative base"""
        base = -2
        num = 32
        self.assertRaises(BadOperandException, self.op.logarithm, num, base)

    def test_both_negative_exception(self):
        """Both base and number are negative"""
        base = -2
        num = -32
        self.assertRaises(BadOperandException, self.op.logarithm, num, base)


@colorize(color=BLUE)
class RootTests(unittest.TestCase):

    def setUp(self) -> None:
        self.op = Advanced()

    def test_basic(self):
        """Basic test"""
        degree = 2
        num = 9
        self.assertEqual(3, self.op.rootn(degree, num))

    def test_negative_base(self):
        """Negative degree"""
        degree = -2
        num = 3
        self.assertEqual(0.5773503, self.op.rootn(degree, num))

    def test_negative_num(self):
        """Negative body"""
        degree = 3
        num = -27
        self.assertEqual(-3, self.op.rootn(degree, num), "Error")

    def test_negative_num_exception(self):
        """Negative radicant (number)"""
        degree = 2
        num = -27
        self.assertRaises(BadOperandException, lambda: self.op.rootn(degree, num))

    def test_float(self):
        degree = 2
        num = 14
        self.assertEqual(3.7416574, self.op.rootn(degree, num))

    def test_zero_radicant(self):
        """Radicant is 0"""
        degree = 3
        num = 0
        self.assertEqual(0, self.op.rootn(degree, num))


if __name__ == '__main__':
    unittest.main()