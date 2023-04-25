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