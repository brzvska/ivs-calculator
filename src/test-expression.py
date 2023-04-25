import unittest
from calculator.calclib.expressions import MathParsing


class AdditionTests(unittest.TestCase):
    print('Testing addition')
    def setUp(self) -> None:
        self.op = MathParsing()

    def test_basic_int(self):
        """Test basic integer"""
        expr = '5+5'
        self.assertEqual('10', self.op.parse(expr))

    def test_basic_float(self):
        """Test basic float"""
        expr = '5.3+6.1'
        self.assertEqual('11.4', self.op.parse(expr))

    def test_basic_neg_int(self):
        """Test basic negative integer"""
        expr = '-10+3'
        self.assertEqual('-7', self.op.parse(expr))

    def test_basic_neg_float(self):
        """Test basic negative float"""
        expr = '9.5+0.1'
        self.assertEqual('9.6', self.op.parse(expr))

    def test_basic_both_neg_int(self):
        """Test basic both negative integers"""
        expr = '-9+(-3)'
        self.assertEqual('-12', self.op.parse(expr))

    def test_basic_both_neg_floats(self):
        """Test basic both negative floats"""
        expr = '-0.1+(-4.4)'
        self.assertEqual('-4.5', self.op.parse(expr))

    def test_basic_operand_is_missing(self):
        """Test one operand is missing"""
        expr = '5+'
        self.assertEqual('Couldn/''t parse expression', self.op.parse(expr))

    def test_basic_expr(self):
        """Test basic expression"""
        expr = '(5+9)+8'
        self.assertEqual('22', self.op.parse(expr))

    def test_complex_expr(self):
        """Test complex expression"""
        expr = '5+5+(3+1+(1+1))'
        self.assertEqual('16', self.op.parse(expr))


class SubtractionTests(unittest.TestCase):
    print('Testing substraction')
    def setUp(self) -> None:
        self.op = MathParsing()

    def test_basic_int(self):
        """Test basic integer"""
        expr = '10-1'
        self.assertEqual('9', self.op.parse(expr))

    def test_basic_float(self):
        """Test basic float"""
        expr = '10.0-1.1'
        self.assertEqual('9.9', self.op.parse(expr))

    def test_basic_neg_int(self):
        """Test basic negative integer"""
        expr = '-5-1'
        self.assertEqual('-6', self.op.parse(expr))

    def test_basic_neg_float(self):
        """Test basic negative float"""
        expr = '-4.4-1.1'
        self.assertEqual('-5.5', self.op.parse(expr))

    def test_basic_both_neg_int(self):
        """Test basic both negative integers"""
        expr = '-5-6'
        self.assertEqual('-11', self.op.parse(expr))

    def test_basic_both_neg_floats(self):
        """Test basic both negative floats"""
        expr = '-1.1-0.1'
        self.assertEqual('-1.2', self.op.MathParsing.parse(expr))

    def test_basic_expr(self):
        """Test basic expression"""
        expr = '-1-(4-3)'
        self.assertEqual('-2', self.op.parse(expr))

    def test_complex_expr(self):
        """Test complex expression"""
        expr = '(-1-(10-5-(1-1)))'
        self.assertEqual('-6', self.op.parse(expr))


class MultiplyTests(unittest.TestCase):
    print('Testing multiplication')
    def setUp(self) -> None:
        self.op = MathParsing()

    def test_basic_int(self):
        """Test basic integer"""
        expr = '10×8'
        self.assertEqual('80', self.op.parse(expr))

    def test_basic_float(self):
        """Test basic float"""
        expr = '10.4×2'
        self.assertEqual('20.8', self.op.parse(expr))

    def test_basic_neg_int(self):
        """Test basic negative integer"""
        expr = '3×(-4)'
        self.assertEqual('-12', self.op.parse(expr))

    def test_basic_neg_float(self):
        """Test basic negative float"""
        expr = '-0.1×3'
        self.assertEqual('-0.3', self.op.parse(expr))

    def basic_test_both_neg_int(self):
        """Test basic both negative integers"""
        expr = '-9×(-2)'
        self.assertEqual('18', self.op.parse(expr))

    def basic_test_both_neg_floats(self):
        """Test basic both negative floats"""
        expr = '-1.1×(-3.4)'
        self.assertEqual('3.74', self.op.parse(expr))

    def test_complex_expr(self):
        """Test complex expression"""
        expr = '5×3×(8×2×1)'
        self.assertEqual('240', self.op.parse(expr))


class DivisionTests(unittest.TestCase):
    print('Testing division')
    def setUp(self) -> None:
        self.op = MathParsing()

    def test_basic_int(self):
        """Test basic integer"""
        expr = '10÷5'
        self.assertEqual('2', self.op.parse(expr))

    def test_basic_float(self):
        """Test basic float"""
        expr = '10.4÷2'
        self.assertEqual('5.2', self.op.parse(expr))

    def test_basic_neg_int(self):
        """Test basic negative integer"""
        expr = '-4÷2'
        self.assertEqual('-2', self.op.parse(expr))

    def test_basic_neg_float(self):
        """Test basic negative float"""
        expr = '4.8÷(-1.2)'
        self.assertEqual('-4', self.op.parse(expr))

    def test_basic_both_neg_int(self):
        """Test basic both negative integers"""
        expr = '-18÷(-3)'
        self.assertEqual('6', self.op.parse(expr))

    def test_basic_both_neg_floats(self):
        """Test basic both negative floats"""
        expr = '-6.6÷(-2.2)'
        self.assertEqual('3', self.op.parse(expr))

    def test_complex_expr(self):
        """Test complex expression"""
        expr = '(-10÷(4÷2))÷1)'
        self.assertEqual('-5', self.op.parse(expr))


class PiTests(unittest.TestCase):
    print('Testing Pi')
    def setUp(self) -> None:
        self.op = MathParsing()

    def test_basic_pi(self):
        """Test basic Pi"""
        expr = 'π'
        self.assertEqual('3.1416', self.op.parse(expr))


class ExponentTests(unittest.TestCase):
    print('Testing exponent')

    def setUp(self) -> None:
        self.op = MathParsing()

    def test_basic_exponent(self):
        expr = 'e'
        self.assertEqual('2.7183', self.op.parse(expr))


class AllOperationsTests(unittest.TestCase):
    print('Testing all operations')

    def setUp(self) -> None:
        self.op = MathParsing()

    def test_basic_add_sub(self):
        """Test basic additing and subsubstraction"""
        expr = '5+3-8'
        self.assertEqual('0', self.op.parse(expr))

    def test_basic_add_sub_2(self):
        """Test n. 2 basic additing and substracting"""
        expr = '-16+8-(4+3-1)'
        self.assertEqual('-14', self.op.parse(expr))

    def test_basic_add_mul(self):
        """Test basic addition and multiplication"""
        expr = '44+(2×6)'
        self.assertEqual('56', self.op.parse(expr))

    def test_basic_add_mul_2(self):
        """Test n. 2 basic addition and multiplication"""
        expr = '((-10)×(-5))+13'
        self.assertEqual('63', self.op.parse(expr))

    def test_basic_sub_mul(self):
        """Test basic substraction and multiplication"""
        expr = '10-(4×4)'
        self.assertEqual('-6', self.op.parse(expr))

    def test_basic_sub_mul_2(self):
        """Test n.2 basic substraction and multiplication"""
        expr = '(848×3)-1000'
        self.assertEqual('1544', self.op.parse(expr))

    def test_basic_add_div(self):
        """Test basic addition and division"""
        expr = '(216÷16)+66'
        self.assertEqual('79.5', self.op.parse(expr))

    def test_basic_add_div_2(self):
        """Test n. 2 basic addition and division"""
        expr = '555+((100÷4)÷10)'
        self.assertEqual('557.5', self.op.parse(expr))

    def test_basic_sub_div(self):
        """Test basic substraction and division"""
        expr = '(1000÷4)-3'
        self.assertEqual('247', self.op.parse(expr))

    def test_basic_sub_div_2(self):
        """Test n. 2 basic subscription and division"""
        expr = '(100-(20÷4))÷5'
        self.assertEqual('19', self.op.parse(expr))

    def test_basic_mul_div(self):
        """Test basic multiplication and division"""
        expr = '(10÷2)×5'
        self.assertEqual('25', self.op.parse(expr))

    def test_all_operations_1(self):
        """Test n. 1 all operations"""
        expr = '93×e-100'
        self.assertEqual('152.8019', self.op.parse(expr))

    def test_all_operations_2(self):
        """Test n. 2 all operations"""
        expr = "((100×5)-(-100))+5×π"
        self.assertEqual('615.708', self.op.parse(expr))

    def test_all_operations_3(self):
        """Test n. 3 all operations"""
        expr = '((-1)×15)+2'
        self.assertEqual('-13', self.op.parse(expr))




if __name__ == '__main__':
    unittest.main()