"""
@package arithmetic
@file basic.py
@author Alina Vinogradova
Implementation of basic mathematical operations for the calculator
"""

"""
Base class "Basic"
Representation of basic mathematical operations
"""
class Basic:
    """
    A class variables:
    pi - constant
    exp - constant
    """
    pi = 3.1416
    exp = 2.7183

    """
    The constructor
    """
    def __init__(self):
        pass

    """
    Method for + operation
    @param x First operand
    @param y Second operand
    @return Sum of two numbers
    """
    def add(self, x: float, y: float):
        return self.int_translate(x + y)

    """
    Method for - operation
    @param minuend First operand
    @param subtrahend Second operand
    @return Difference between two numbers
    """
    def sub(self, minuend: float, subtrahend: float):
        return self.int_translate(minuend - subtrahend)

    """
    Method for * operation
    @param multiplier First operand
    @param multiplicand Second operand
    @return Product of two numbers
    """
    def mul(self, multiplier: float, multiplicant: float):
        return self.int_translate(multiplier * multiplicant)

    """
    Method for / operation
    @param dividend The number to be divided
    @param divisor The number to divide by
    @return Division operation result
    """
    def div(self, divident: float, divisor: float):
        if divisor == 0:
            raise ZeroDivisionError
        else:
            return self.int_translate(divident / divisor)


    @staticmethod
    def int_translate(num):
        if isinstance(num, complex):
            num = num.real
        if float(num).is_integer():
            return int(num)
        else:
            return round(num, 7)

