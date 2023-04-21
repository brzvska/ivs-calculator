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
        self.assertEqual(self.op.add(x, y), 3.0)

    def test_comp(self):
        """Compatibility with integers"""
        x = 3
        y = 4
        print("Testing (3 + 4)...")
        self.assertEqual(self.op.add(x, y), 7)

    def test_float(self):
        """Simple float numbers"""
        x = 4.3
        y = 2.6
        print("Testing (4.3 + 2.6)...")
        self.assertEqual(self.op.add(x, y), 6.9)

    def test_zero(self):
        """Two zeros"""
        x = 0
        y = 0
        print("Testing (0 + 0)...")
        self.assertEqual(self.op.add(x, y), 0)

    def test_negative_both(self):
        """Two negative numbers"""
        x = -5
        y = -10
        print("Testing (-5 + -10)...")
        self.assertEqual(self.op.add(x, y), -15)

    def test_negative_one(self):
        """One negative number"""
        x = -5
        y = 15
        print("Testing (-5 + 15)...")
        self.assertEqual(self.op.add(x, y), 10)

    def test_negative_zero(self):
        """Sum two non-zeros is zero"""
        x = -5
        y = 5
        print("Testing (-5 + 5)...")
        self.assertEqual(self.op.add(x, y), 0)

    def test_extreme(self):
        """Two very large numbers"""
        x = 159687234
        y = 623903476
        print("Testing very large numbers...")
        self.assertEqual(self.op.add(x, y), 783590710)

    def test_long_float(self):
        """Two long floats"""
        x = 125.435735
        y = 87.32612747
        print("Testing long floats...")
        self.assertEqual(self.op.add(x, y), 212.76186247)


class SubTests(unittest.TestCase):
    print("\tTesting subtraction operation")

    def setUp(self) -> None:
        self.op = Basic()

    def test_default(self):
        """Basic"""
        x = 17.0
        y = 5.0
        print("Testing (17.0 - 5.0)...")
        self.assertEqual(self.op.sub(x, y), 12.0)

    def test_comp(self):
        """Compatibility with integers"""
        x = 25
        y = 16
        print("Testing (25 - 16)...")
        self.assertEqual(self.op.sub(x, y), 9)

    def test_float(self):
        """Float numbers"""
        x = 39.7
        y = 22.9
        print("Testing (39.7 - 22.9)...")
        self.assertEqual(self.op.sub(x, y), 16.8)

    def test_zero(self):
        """Two zeros"""
        x = 0
        y = 0
        print("Testing (0 - 0)...")
        self.assertEqual(self.op.sub(x, y), 0)

    def test_negative_both(self):
        """Two negative numbers"""
        x = -5
        y = -10
        print("Testing (-5 - -10)...")
        self.assertEqual(self.op.sub(x, y), 5)

    def test_negative_one(self):
        """One negative"""
        x = -5
        y = 15
        print("Testing (-5 - 15)...")
        self.assertEqual(self.op.sub(x, y), -20)

    def test_negative_zero(self):
        """Sub is zero"""
        x = -5
        y = -5
        print("Testing (-5 - -5)...")
        self.assertEqual(self.op.sub(x, y), 0)

    def test_extreme(self):
        """Two very large numbers"""
        x = 623903476
        y = 159687234
        print("Testing very large numbers...")
        self.assertEqual(self.op.sub(x, y), 464216242)

    def test_long_float(self):
        """Two long floats"""
        x = 3252.12612686
        y = 2637.865946
        print("Testing long floats...")
        self.assertEqual(self.op.sub(x, y), 614.26018086)


class MulTests(unittest.TestCase):
    print("\tTesting multiplication operation")

    def setUp(self) -> None:
        self.op = Basic()

    def test_default(self):
        """Basic"""
        x = 5.0
        y = 3.0
        print("Testing (5.0 * 3.0)...")
        self.assertEqual(self.op.mul(x, y), 15.0)

    def test_comp(self):
        """Compatibility with integers"""
        x = 7
        y = 5
        print("Testing (7 * 5)...")
        self.assertEqual(self.op.mul(x, y), 35)

    def test_float(self):
        """Float numbers"""
        x = 6.7
        y = 4.9
        print("Testing (6.7 * 4.9)...")
        self.assertEqual(self.op.mul(x, y), 32.83)

    def test_zero(self):
        """Two zeros"""
        x = 0
        y = 0
        print("Testing (0 * 0)...")
        self.assertEqual(self.op.mul(x, y), 0)

    def test_negative_both(self):
        """Two negative numbers"""
        x = -10
        y = -3
        print("Testing (-10 * -3)...")
        self.assertEqual(self.op.mul(x, y), 30)

    def test_negative_one(self):
        """One negative"""
        x = 6
        y = -8
        print("Testing (6 * -8)...")
        self.assertEqual(self.op.mul(x, y), -48)

    def test_negative_zero(self):
        """Sub is zero"""
        x = -33
        y = 0
        print("Testing (-33 * 0)...")
        self.assertEqual(self.op.mul(x, y), 0)

    def test_extreme(self):
        """Two very large numbers"""
        x = 303802
        y = 861860
        print("Testing very large numbers...")
        self.assertEqual(self.op.mul(x, y), 261834791720)

    def test_long_float(self):
        """Two long floats"""
        x = 12612.174389
        y = 236.539653463
        print("Testing long floats...")
        self.assertEqual(self.op.mul(x, y), 2983279.359388983759107)


class DivTests(unittest.TestCase):
    print("\tTesting division operation")

    def setUp(self) -> None:
        self.op = Basic()

    def test_default(self):
        """Basic"""
        x = 10.0
        y = 2.0
        print("Testing (10.0 / 2.0)...")
        self.assertEqual(self.op.div(x, y), 5.0)

    def test_comp(self):
        """Compatibility with integers"""
        x = 21
        y = 7
        print("Testing (21 / 7)...")
        self.assertEqual(self.op.div(x, y), 3)

    def test_float(self):
        """Float numbers"""
        x = 111.622
        y = 3.4
        print("Testing (111.622 / 3.4)...")
        self.assertEqual(self.op.div(x, y), 32.83)

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
        self.assertEqual(self.op.div(x, y), 2.5)

    def test_negative_one(self):
        """One negative"""
        x = 6
        y = -8
        print("Testing (6 / -8)...")
        self.assertEqual(self.op.div(x, y), -0.75)

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
        self.assertEqual(self.op.div(x, y), 19.7235410021)

    def test_long_float(self):
        """Two long floats"""
        x = 12612.174389
        y = 236.539653463
        print("Testing long floats...")
        self.assertEqual(self.op.div(x, y), 53.319492966)
