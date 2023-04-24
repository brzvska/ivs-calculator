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
    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y

    # Static method for - operation
    # @param minuend First operand
    # @param subtrahend Second operand
    # @return Difference between two numbers
    @staticmethod
    def sub(minuend: float, subtrahend: float) -> float:
        return minuend - subtrahend

    # Static method for * operation
    # @param multiplier First operand
    # @param multiplicand Second operand
    # @return Product of two numbers
    @staticmethod
    def mul(multiplier: float, multiplicant: float) -> float:
        return multiplier * multiplicant

    # Static method for / operation
    # @param dividend The number to be divided
    # @param divisor The number to divide by
    # @return Division operation result
    @staticmethod
    def div(divident: float, divisor: float) -> float:
        try:
            return divident / divisor
        except ZeroDivisionError:
            print("Error! Denominator can not be 0")