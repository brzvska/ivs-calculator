# @package arithmetic
# @file basic.py
# Implementation of advanced mathematical operations for the calculator
import sys

from .basic import Basic
from .exceptions import BadOperandException
import math


# Base class "Advanced"
# Representation of advanced mathematical operations
class Advanced(Basic):
    # The constructor
    def __init__(self):
        super().__init__()

    # Static method for exponentiation operation
    # @param base Base number
    # @param exponent Exponent number
    # @return Power of the given number
    @staticmethod
    def power(base: float, exponent: int) -> float:
        return pow(base, exponent)

    # Static method for factorial computation
    # @param x Operand
    # @return Factorial of a given number, -1 if error occured
    @staticmethod
    def factorial(x: int) -> int:
        try:
            if x < 0:
                raise BadOperandException

            result = 1
            for num in range(1, x + 1):
                result = result * num
            return result
        except BadOperandException:
            sys.stderr.write("Error: wrong factorial operand")

    # Static method for logarithms computation
    # @param base Base number
    # @param number Antilogarithm number
    # @return Logarithm value of given number with specific base
    @staticmethod
    def logarithm(number: int, base: int) -> float:
        try:
            if base == 1 or base <= 0 or number <= 0:
                raise BadOperandException
            return math.log(number, base)
        except BadOperandException:
            sys.stderr.write("Error: wrong logarithm base")


    # Method for n-th root computations
    # @param self Object pointer
    # @param degree Root degree
    # @param radicant The number from which the root has to be extracted
    def rootn(self, degree: int, radicand: float):
        try:
            if degree % 2 == 0 and radicand < 0:
                raise BadOperandException
            return radicand**(self.div(1, degree))
        except BadOperandException:
            sys.stderr.write("Error: wrong root expression")


    # Static method for sinus function
    # @param x An angle in radians (pi/2, pi/4, pi/3, etc.)
    # @return The sine of the given parameter value
    @staticmethod
    def sinus(x):
        return math.sin(x)

    # Static method for cosines function
    # @param x An angle in radians (pi/2, pi/4, pi/3, etc.)
    # @return The cosine of the given parameter value
    @staticmethod
    def cosines(x):
        return math.cos(x)

    # Method for tangents function
    # @param x An angle in radians (pi/2, pi/4, pi/3, etc.)
    # @return The tangent  of the given parameter value
    def tang(self, x):
        return self.div(self.sinus(x), self.cosines(x))

    # Method for cotangents function
    # @param x An angle in radians (pi/2, pi/4, pi/3, etc.)
    # @return The cotangent  of the given parameter value
    def cotg(self, x):
        return self.div(self.cosines(x), self.sinus(x))
