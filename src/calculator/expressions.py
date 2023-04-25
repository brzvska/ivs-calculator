"""
@package calculator
@file expressions.py
@author Maryia Mazurava
Implementation of math logic
"""

from stack import Stack
from arithmetic.basic import Basic
from arithmetic.advanced import Advanced

LEFT_PAR = "("
RIGHT_PAR = ")"


"""
Base class "BasicMathParsing"
Representation of basic math logic
"""
class MathParsing:

    """ Constructor """
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '×': 2, '÷': 2, '^': 3}
        self.adv = Advanced()
        self.basic = Basic()
        self.tokens = []
        self.operator_stack = Stack()
        self.operand_stack = Stack()

    """
    Method for splitting an expression into tokens
    @param expression Expression string
    """
    def split_expression(self, expression: str):
        number = ""
        for char in expression:
            if char.isnumeric() or char == ".":
                number += char
            elif char == RIGHT_PAR or char == LEFT_PAR or char in self.operators:
                if len(number) != 0:
                    self.tokens.append(number)
                    number = ""
                self.tokens.append(char)
            elif char == "e":
                self.tokens.append("2.7183")
            elif char == "π":
                self.tokens.append("3.1416")
        if number != "":
            self.tokens.append(number)

    """
    Method for checking if the expression is correct
    @return True if expression is correct, False instead
    """
    def check_semantics(self):
        """ Parentheses balance checking """
        pars = []
        for token in self.tokens:
            if token == LEFT_PAR:
                pars.append(token)
            elif token == RIGHT_PAR:
                if not pars:
                    return False
                pars.pop()
        if pars:
            return False

        """ Checking if the operators are used correctly """
        prev_token = None
        for token in self.tokens:
            if prev_token is None:
                prev_token = token
            elif token in self.operators:
                if prev_token in self.operators:
                    return False
                elif prev_token == LEFT_PAR and token != "-":
                    return False
                prev_token = token
            elif token == LEFT_PAR:
                if prev_token == LEFT_PAR or prev_token in self.operators:
                    prev_token = token
                else:
                    return False
            else:
                prev_token = token

        if self.tokens[-1] in self.operators or self.tokens[-1] == LEFT_PAR:
            return False

        """ Checking the number format and possible negative numbers """
        prev_token = None
        for token in self.tokens:
            if prev_token is None:
                prev_token = token
                index = self.tokens.index(prev_token)
                if prev_token == "-" and self.tokens[index + 1][0].isnumeric():
                    self.tokens[index] += self.tokens[index + 1]
                    del self.tokens[index + 1]
                    pass
            if token not in self.operators and token != RIGHT_PAR and token != LEFT_PAR:
                if token[0] == ".":
                    return False
                if "." in token:
                    count = 0
                    for c in token:
                        if c == ".":
                            count += 1
                    if count > 1:
                        return False
                    else:
                        prev_token = token
                if len(token) >= 2:
                    print("here")
                    if token[0] == "0" and token[1] != ".":
                        return False
                if prev_token == "-":
                    index = self.tokens.index(prev_token)
                    if self.tokens[index - 1] == LEFT_PAR:
                        self.tokens[index] += self.tokens[index + 1]
                        del self.tokens[index + 1]

            prev_token = token

        return True

    """
    Main method for parsing the expression using stack.py module
    @param expression Expression string from app.py module
    @return Result string of the expression or error message
    """
    def parse(self, expression: str):
        if len(expression) > 3 and expression[0:3] == "log":
            result, index = self.parse_advanced("log", expression)
            if result == "":
                return "Couldn't parse expression"
            expression = expression.replace(expression[:index], result)
        if len(expression) > 4 and expression[0:4] == "sqrt":
            result, index = self.parse_advanced("sqrt", expression)
            if result == "":
                return "Couldn't parse expression"
            expression = expression.replace(expression[:index], result)
        if len(expression) == 0:
            return "Enter math expression"

        self.split_expression(expression)

        if self.check_semantics() is False:
            return "Couldn't parse expression"

        """ Start parsing an expression """
        for token in self.tokens:
            if token not in self.operators and token != LEFT_PAR and token != RIGHT_PAR:
                self.operand_stack.push(token)
            elif token == LEFT_PAR:
                self.operator_stack.push(token)
            elif token == RIGHT_PAR:
                while not self.operator_stack.top() == LEFT_PAR:
                    operand2 = float(self.operand_stack.pop())
                    operand1 = float(self.operand_stack.pop())
                    if self.evaluate(operand1, operand2) is False:
                        return "Couldn't parse expression"
                if not self.operator_stack.is_empty() and self.operator_stack.top() == LEFT_PAR:
                    self.operator_stack.pop()
            elif token in self.operators:
                if self.operator_stack.is_empty():
                    self.operator_stack.push(token)
                else:
                    top = self.operator_stack.top()
                    if top == LEFT_PAR:
                        self.operator_stack.push(token)
                    elif self.operators[token] > self.operators[top]:
                        self.operator_stack.push(token)
                    else:
                        operand2 = float(self.operand_stack.pop())
                        operand1 = float(self.operand_stack.pop())
                        if self.evaluate(operand1, operand2) is False:
                            return "Couldn't parse expression"

                        self.operator_stack.push(token)

        while not self.operator_stack.is_empty():
            operand2 = float(self.operand_stack.pop())
            operand1 = float(self.operand_stack.pop())
            if self.evaluate(operand1, operand2) is False:
                return "Couldn't parse expression"

        self.tokens = []

        return str(self.operand_stack.top())

    """
    Main method for parsing the expression using stack.py module
    @param func Function name (log or sqrt)
    @param exspression Expression to evaluate
    @return Result of the parsing. Result is "" if error occurred
    """
    def parse_advanced(self, func, expression):
        if func == "sqrt":
            result = ""
            degree = ""
            base = ""
            start = None
            par_count = 0
            for char in expression[4:]:
                if char == LEFT_PAR:
                    par_count += 1
                if char == RIGHT_PAR:
                    par_count -= 1

                degree += char

                if char == RIGHT_PAR and par_count == 0:
                    index = expression.index(char)
                    start = char
                    break

            par_count = 0
            if start == RIGHT_PAR:
                index_end = index + 1
                for char in expression[index + 1:]:
                    if char == LEFT_PAR:
                        par_count += 1
                    if char == RIGHT_PAR:
                        par_count -= 1

                    base += char
                    index_end += 1

                    if char == RIGHT_PAR and par_count == 0:
                        break

            if degree != "()" and base != "()":
                degree_res = self.parse(degree)
                base_res = self.parse(base)

                if base_res != "Couldn't parse expression" and degree_res != "Couldn't parse expression":
                    if degree_res.isnumeric():
                        result = self.adv.rootn(int(degree_res), float(base_res))
        else:
            result = ""
            degree = ""
            base = ""
            start = None
            par_count = 0
            for char in expression[3:]:
                if char == LEFT_PAR:
                    par_count += 1
                if char == RIGHT_PAR:
                    par_count -= 1

                degree += char

                if char == RIGHT_PAR and par_count == 0:
                    index = expression.index(char)
                    start = char
                    break

            par_count = 0
            if start == RIGHT_PAR:
                index_end = index + 1
                for char in expression[index + 1:]:
                    if char == LEFT_PAR:
                        par_count += 1
                    if char == RIGHT_PAR:
                        par_count -= 1

                    base += char
                    index_end += 1

                    if char == RIGHT_PAR and par_count == 0:
                        break

            if degree != "()" and base != "()":
                degree_res = self.parse(degree)
                base_res = self.parse(base)

                if base_res != "Couldn't parse expression" and degree_res != "Couldn't parse expression":
                    if degree_res.isnumeric():
                        result = self.adv.logarithm(float(base_res), int(degree_res))

        return str(result), index_end

    """
    Method for evaluating factorial
    @param exspression Expression to evaluate
    @return Result of the evaluating
    """
    def parse_factorial(self, expression):
        expression_evaluate = ""
        for char in expression:
            expression_evaluate += char

        parse_result = self.parse(expression_evaluate)
        if parse_result.isnumeric():
            if int(parse_result) > 0:
                result = self.adv.factorial(int(parse_result))
        else:
            result = "Couldn't parse expression"

        return str(result)

    """
    Method for evaluating trigonometric functions
    @param func Trigonometric function
    @param exspression Expression to evaluate
    @return Result of the evaluating
    """
    def parse_trigonometry(self, func, expression):
        expression_evaluate = ""
        for char in expression:
            expression_evaluate += char

        parse_result = float(self.parse(expression_evaluate))
        match func:
            case "sin":
                result = self.adv.sinus(parse_result)
            case "cos":
                result = self.adv.cosines(parse_result)
            case "tan":
                result = self.adv.tang(parse_result)
            case "ctg":
                result = self.adv.cotg(parse_result)

        return str(result)


    """
    Method for evaluation of single math expressions using math libraries
    @param operand1 First operand
    @param operand2 Second operand
    @return False if error occurred
    """
    def evaluate(self, operand1, operand2):
        match self.operator_stack.pop():
            case "-":
                result = self.basic.sub(operand1, operand2)
            case "+":
                result = self.basic.add(operand1, operand2)
            case "×":
                result = self.basic.mul(operand1, operand2)
            case "÷":
                result = self.basic.div(operand1, operand2)
            case "^":
                if operand2.is_integer():
                    result = self.adv.power(operand1, operand2)
                else:
                    return False

        self.operand_stack.push(result)


