import unittest

from src.arithmetic.advanced import Advanced


class Power(unittest.TestCase):
    print("\tTesting power operation")

    def setUp(self) -> None:
        self.op = Advanced()

    def test_square(self):
        """Basic power of 2"""
        base = 5
        exp = 2
        self.assertEqual(self.op.power(5, 2), 25)

    def test_exp(self):
        """Test exponent"""
        base = 2
        exp = 10
        self.assertEqual(self.op.power(2, 10), 1024)