# @package arithmetic
# @file basic.py
# Implementation of basic mathematical operations for the calculator


# Base class "Basic"
# Representation of basic mathematical operations
class Basic:
    # A class variables:
    # pi - constant
    # exp - constant
    pi = 3.14
    exp = 2.72

    # The constructor
    def __init__(self):
        pass

    # Static method for + operation
    # @param x First operand
    # @param y Second operand
    # @return Sum of two numbers
    def add(self, x: float, y: float):
        return self.int_translate(x + y)

    # Static method for - operation
    # @param minuend First operand
    # @param subtrahend Second operand
    # @return Difference between two numbers
    def sub(self, minuend: float, subtrahend: float):
        return self.int_translate(minuend - subtrahend)

    # Static method for * operation
    # @param multiplier First operand
    # @param multiplicand Second operand
    # @return Product of two numbers
    def mul(self, multiplier: float, multiplicant: float):
        return self.int_translate(multiplier * multiplicant)

    # Static method for / operation
    # @param dividend The number to be divided
    # @param divisor The number to divide by
    # @return Division operation result
    def div(self, divident: float, divisor: float) -> float:
        try:
            return self.int_translate(divident / divisor)
        except ZeroDivisionError:
            print("Error! Denominator can not be 0")

    @staticmethod
    def int_translate(num):
        if float(num).is_integer():
            return int(num)
        else:
            return round(num, 7)

