from stack import Stack
import re
# from src.arithmetic.basic import Basic


LEFT_PAR = "("
RIGHT_PAR = ")"
PLUS = "+"
MINUS = "-"
MUL = "*"
DIV = "/"

class BasicMathParsing:
    tokens = []

    def __init__(self):
        self.operators = {'+': 1, '-': 1, '×': 2, '÷': 2}

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
            # else:
            #     return False

        if number != "":
            self.tokens.append(number)

    def check_semantics(self):
        # Pars checking
        pars = []
        for token in self.tokens:
            if token == '(':
                pars.append(token)
            elif token == ')':
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
                elif prev_token == LEFT_PAR and token != MINUS:
                    return False
                prev_token = token
            elif token == LEFT_PAR:
                if prev_token == LEFT_PAR or prev_token in self.operators:
                    prev_token = token
                else:
                    return False
            else:
                prev_token = token

        if self.tokens[-1] in self.operators or self.tokens[-1] == '(':
            return False

        # Checking the number format
        prev_token = None
        for token in self.tokens:
            if prev_token is None:
                prev_token = token
                index = self.tokens.index(prev_token)
                if prev_token == MINUS and self.tokens[index + 1][0].isnumeric():
                    self.tokens[index] += self.tokens[index + 1]
                    del self.tokens[index + 1]
                    prev_token = self.tokens[index]
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
                if token[0] == "0" and token[1] != ".":
                    return False
                if prev_token == MINUS:
                    index = self.tokens.index(prev_token)
                    if self.tokens[index - 1] == LEFT_PAR:
                        self.tokens[index] += self.tokens[index + 1]
                        del self.tokens[index + 1]
                        prev_token = self.tokens[index]

            prev_token = token

        return True

    def parse(self, expression):
        self.split_expression(expression)

        if self.check_semantics() is False:
            print("Wrong semantics")
            return "error"
        operator_stack = Stack()
        operand_stack = Stack()
        # ['9', '*', '9', '+', '8']
        for token in self.tokens:
            if token not in self.operators and token != LEFT_PAR and token != RIGHT_PAR:
                operand_stack.push(token)
            elif token == LEFT_PAR:
                operator_stack.push(token)
            elif token == RIGHT_PAR:
                if operator_stack.top() == LEFT_PAR:
                    operator_stack.pop()
                while not operator_stack.top() == LEFT_PAR:
                    operand2 = float(operand_stack.pop())
                    operand1 = float(operand_stack.pop())
                    # basic = Basic()
                    match operator_stack.pop():
                        case "-":
                            result = operand1 - operand2
                            operand_stack.push(result)
                        case "+":
                            result = operand1 + operand2
                            operand_stack.push(result)
                        case "×":
                            result = operand1 * operand2
                            operand_stack.push(result)
                        case "÷":
                            if operand2 == "0":
                                return "false"
                            result = operand1 / operand2
                            operand_stack.push(result)
                if not operator_stack.is_empty() and operator_stack.top() == LEFT_PAR:
                    operator_stack.pop()
            elif token in self.operators:
                if operator_stack.is_empty():
                    operator_stack.push(token)
                else:
                    top = operator_stack.top()
                    if top == LEFT_PAR:
                        operator_stack.push(token)
                    elif self.operators[token] > self.operators[top]:
                        operator_stack.push(token)
                    else:
                        operand2 = float(operand_stack.pop())
                        operand1 = float(operand_stack.pop())
                        # basic = Basic()
                        match operator_stack.pop():
                            case "-":
                                result = operand1 - operand2
                                operand_stack.push(result)
                            case "+":
                                result = operand1 + operand2
                                operand_stack.push(result)
                            case "×":
                                result = operand1 * operand2
                                operand_stack.push(result)
                            case "÷":
                                if operand2 == "0":
                                    return "false"
                                result = operand1 / operand2
                                operand_stack.push(result)

                        operator_stack.push(token)

        while not operator_stack.is_empty():
            operand2 = float(operand_stack.pop())
            operand1 = float(operand_stack.pop())
            # basic = Basic()
            match operator_stack.pop():
                case "-":
                    result = operand1 - operand2
                    operand_stack.push(result)
                case "+":
                    result = operand1 + operand2
                    operand_stack.push(result)
                case "×":
                    result = operand1 * operand2
                    operand_stack.push(result)
                case "÷":
                    if operand2 == "0":
                        return "false"
                    result = operand1 / operand2
                    operand_stack.push(result)

        return str(operand_stack.top())


if __name__ == '__main__':
    expression = "-5+(3×2+4×3)÷3"
    inst = BasicMathParsing()
    result = inst.parse(expression)
    print(result)
    print("RABOTAET!!!")

