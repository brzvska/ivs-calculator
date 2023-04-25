from stack import Stack
import re

from arithmetic.basic import Basic
from arithmetic.advanced import Advanced

LEFT_PAR = "("
RIGHT_PAR = ")"


class BasicMathParsing:
    tokens = []
    operator_stack = Stack()
    operand_stack = Stack()

    def __init__(self):
        self.operators = {'+': 1, '-': 1, '×': 2, '÷': 2}
        self.adv = Advanced()
        self.basic = Basic()

    def split_expression(self, expression):
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

    def check_semantics(self):
        # Pars checking
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

        # Check if the operators are used correctly
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

        # Checking the number format
        prev_token = None
        for token in self.tokens:
            if prev_token is None:
                prev_token = token
                index = self.tokens.index(prev_token)
                if prev_token == "-" and self.tokens[index + 1][0].isnumeric():
                    self.tokens[index] += self.tokens[index + 1]
                    del self.tokens[index + 1]
            elif token not in self.operators and token != RIGHT_PAR and token != LEFT_PAR:
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
                    if token[0] == "0" and token[1] != ".":
                        return False
                if prev_token == "-":
                    index = self.tokens.index(prev_token)
                    if self.tokens[index - 1] == LEFT_PAR:
                        self.tokens[index] += self.tokens[index + 1]
                        del self.tokens[index + 1]

            prev_token = token

        return True

    def parse(self, expression):
        self.split_expression(expression)
        print(self.tokens)
        if self.check_semantics() is False:
            return "Couldn't parse expression."
        for token in self.tokens:
            if token not in self.operators and token != LEFT_PAR and token != RIGHT_PAR:
                self.operand_stack.push(token)
            elif token == LEFT_PAR:
                self.operator_stack.push(token)
            elif token == RIGHT_PAR:
                while not self.operator_stack.top() == LEFT_PAR:
                    operand2 = float(self.operand_stack.pop())
                    operand1 = float(self.operand_stack.pop())
                    self.evaluate(operand1, operand2)
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
                        self.evaluate(operand1, operand2)

                        self.operator_stack.push(token)

        while not self.operator_stack.is_empty():
            operand2 = float(self.operand_stack.pop())
            operand1 = float(self.operand_stack.pop())
            self.evaluate(operand1, operand2)

        return str(self.operand_stack.top())

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

        self.operand_stack.push(result)


if __name__ == '__main__':
    expression = "-7÷π+6"
    inst = BasicMathParsing()
    result = inst.parse(expression)
    print(result)

