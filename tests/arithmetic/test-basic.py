import unittest
from unittest_prettify.colorize import (
    colorize,
    GREEN,
    RED
)

from src.arithmetic.basic import Basic

@colorize(color=GREEN)
class AddTests(unittest.TestCase):
    print("\tTesting addition operation")

    def setUp(self) -> None:
        self.op = Basic()

    def test_default(self):
        """Basic"""
        x = 1.0
        y = 2.0
        print("Testing (1.0 + 2.0)...")
        self.assertEqual(3.0, self.op.add(x, y))

    def test_comp(self):
        """Compatibility with integers"""
        x = 3
        y = 4
        print("Testing (3 + 4)...")
        self.assertEqual(7, self.op.add(x, y))

    def test_float(self):
        """Simple float numbers"""
        x = 4.3
        y = 2.6
        print("Testing (4.3 + 2.6)...")
        self.assertEqual(6.9, self.op.add(x, y))

    def test_zero(self):
        """Two zeros"""
        x = 0
        y = 0
        print("Testing (0 + 0)...")
        self.assertEqual(0, self.op.add(x, y))

    def test_negative_both(self):
        """Two negative numbers"""
        x = -5
        y = -10
        print("Testing (-5 + -10)...")
        self.assertEqual(-15, self.op.add(x, y))

    def test_negative_one(self):
        """One negative number"""
        x = -5
        y = 15
        print("Testing (-5 + 15)...")
        self.assertEqual(10, self.op.add(x, y))

    def test_negative_zero(self):
        """Sum two non-zeros is zero"""
        x = -5
        y = 5
        print("Testing (-5 + 5)...")
        self.assertEqual(0, self.op.add(x, y))

    def test_extreme(self):
        """Two very large numbers"""
        x = 159687234
        y = 623903476
        print("Testing very large numbers...")
        self.assertEqual(783590710, self.op.add(x, y))

    def test_long_float(self):
        """Two long floats"""
        x = 125.435735
        y = 87.32612747
        print("Testing long floats...")
        self.assertEqual(212.76186247, self.op.add(x, y))


class SubTests(unittest.TestCase):
    print("\tTesting subtraction operation")

    def setUp(self) -> None:
        self.op = Basic()

    def test_default(self):
        """Basic"""
        x = 17.0
        y = 5.0
        print("Testing (17.0 - 5.0)...")
        self.assertEqual(12.0, self.op.sub(x, y))

    def test_comp(self):
        """Compatibility with integers"""
        x = 25
        y = 16
        print("Testing (25 - 16)...")
        self.assertEqual(9, self.op.sub(x, y))

    def test_float(self):
        """Float numbers"""
        x = 39.7
        y = 22.9
        print("Testing (39.7 - 22.9)...")
        self.assertEqual(16.8, self.op.sub(x, y))

    def test_zero(self):
        """Two zeros"""
        x = 0
        y = 0
        print("Testing (0 - 0)...")
        self.assertEqual(0, self.op.sub(x, y))

    def test_negative_both(self):
        """Two negative numbers"""
        x = -5
        y = -10
        print("Testing (-5 - -10)...")
        self.assertEqual(5, self.op.sub(x, y))

    def test_negative_one(self):
        """One negative"""
        x = -5
        y = 15
        print("Testing (-5 - 15)...")
        self.assertEqual(-20, self.op.sub(x, y))

    def test_negative_zero(self):
        """Sub is zero"""
        x = -5
        y = -5
        print("Testing (-5 - -5)...")
        self.assertEqual(0, self.op.sub(x, y))

    def test_extreme(self):
        """Two very large numbers"""
        x = 623903476
        y = 159687234
        print("Testing very large numbers...")
        self.assertEqual(464216242, self.op.sub(x, y))

    def test_long_float(self):
        """Two long floats"""
        x = 3252.12612686
        y = 2637.865946
        print("Testing long floats...")
        self.assertEqual(614.26018086, self.op.sub(x, y))


class MulTests(unittest.TestCase):
    print("\tTesting multiplication operation")

    def setUp(self) -> None:
        self.op = Basic()

    def test_default(self):
        """Basic"""
        x = 5.0
        y = 3.0
        print("Testing (5.0 * 3.0)...")
        self.assertEqual(15.0, self.op.mul(x, y))

    def test_comp(self):
        """Compatibility with integers"""
        x = 7
        y = 5
        print("Testing (7 * 5)...")
        self.assertEqual(35, self.op.mul(x, y))

    def test_float(self):
        """Float numbers"""
        x = 6.7
        y = 4.9
        print("Testing (6.7 * 4.9)...")
        self.assertEqual(32.83, self.op.mul(x, y))

    def test_zero(self):
        """Two zeros"""
        x = 0
        y = 0
        print("Testing (0 * 0)...")
        self.assertEqual(0, self.op.mul(x, y))

    def test_negative_both(self):
        """Two negative numbers"""
        x = -10
        y = -3
        print("Testing (-10 * -3)...")
        self.assertEqual(30, self.op.mul(x, y))

    def test_negative_one(self):
        """One negative"""
        x = 6
        y = -8
        print("Testing (6 * -8)...")
        self.assertEqual(-48, self.op.mul(x, y))

    def test_negative_zero(self):
        """Sub is zero"""
        x = -33
        y = 0
        print("Testing (-33 * 0)...")
        self.assertEqual(0, self.op.mul(x, y))

    def test_extreme(self):
        """Two very large numbers"""
        x = 303802
        y = 861860
        print("Testing very large numbers...")
        self.assertEqual(261834791720, self.op.mul(x, y))

    def test_long_float(self):
        """Two long floats"""
        x = 12612.174389
        y = 236.539653463
        print("Testing long floats...")
        self.assertEqual(2983279.359388983759107, self.op.mul(x, y))


class DivTests(unittest.TestCase):
    print("\tTesting division operation")

    def setUp(self) -> None:
        self.op = Basic()

    def test_default(self):
        """Basic"""
        x = 10.0
        y = 2.0
        print("Testing (10.0 / 2.0)...")
        self.assertEqual(5.0, self.op.div(x, y))

    def test_comp(self):
        """Compatibility with integers"""
        x = 21
        y = 7
        print("Testing (21 / 7)...")
        self.assertEqual(3, self.op.div(x, y))

    def test_float(self):
        """Float numbers"""
        x = 111.622
        y = 3.4
        print("Testing (111.622 / 3.4)...")
        self.assertEqual(32.83, self.op.div(x, y))

    def test_zero(self):
        """Two zeros"""
        x = 0
        y = 0
        print("Testing (0 / 0)...")
        self.failureException(self.op.div(x, y))

    def test_negative_both(self):
        """Two negative numbers"""
        x = -10
        y = -4
        print("Testing (-10 / -4)...")
        self.assertEqual(2.5, self.op.div(x, y))

    def test_negative_one(self):
        """One negative"""
        x = 6
        y = -8
        print("Testing (6 / -8)...")
        self.assertEqual(-0.75, self.op.div(x, y))

    def test_negative_zero(self):
        """Zero Division"""
        x = -33
        y = 0
        print("Testing (-33 / 0)...")
        self.failureException(self.op.div(x, y))

    def test_extreme(self):
        """Two very large numbers"""
        x = 1261281
        y = 63948
        print("Testing very large numbers...")
        self.assertEqual(19.7235410021, self.op.div(x, y))

    def test_long_float(self):
        """Two long floats"""
        x = 12612.174389
        y = 236.539653463
        print("Testing long floats...")
        self.assertEqual(53.319492966, self.op.div(x, y))
