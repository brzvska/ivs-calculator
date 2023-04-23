import unittest

from src.arithmetic.advanced import Advanced
from src.arithmetic.exceptions import BadOperandException


class PowerTests(unittest.TestCase):
    print("\tTesting power operation")

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
        self.assertEqual(2063.66684176, self.op.power(base, exp))


class FactorialTests(unittest.TestCase):
    print("\tTesting factorial operation")

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
        self.assertEqual(None, self.op.factorial(num))

    def test_bigger(self):
        """Some mid number"""
        num = 10
        self.assertEqual(3628800, self.op.factorial(num))

    #todo: float test


class LogarithmTests(unittest.TestCase):
    print("\tTesting logarithm operation")

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
        self.assertEqual(None, self.op.logarithm(num, base))

    def test_negative_num(self):
        """Negative log body"""
        base = 3
        num = -27
        self.assertEqual(None, self.op.logarithm(num, base))

    def test_both_negative(self):
        """Negative both base and number"""
        base = -3
        num = -10
        self.assertEqual(None, self.op.logarithm(num, base))

    def test_float_result(self):
        base = 2
        num = 15
        self.assertEqual(3.90689059561, self.op.logarithm(num, base))


class RootTests(unittest.TestCase):
    print("\tTesting root operation")

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
        self.assertEqual(0.577350269, self.op.rootn(degree, num))

    def test_negative_num(self):
        """Negative body"""
        degree = 3
        num = -27
        self.assertEqual(-3, self.op.rootn(degree, num), "Error")

    def test_float(self):
        degree = 2
        num = 14
        self.assertEqual(3.74165738677, self.op.rootn(degree, num))
