class BasicMath:
    
    def __init__(self, number) -> None:
        self.number = number

    def add(self, x):
        return self.number + x
    
    def sub(self, x):
        return self.number - x
    
    def mul(self, x):
        return self.number * x
    
    def div(self, x):
        if x == 0:
            print("division by zero") 
        else:
            return self.number / x
        
    def percent(self, number):
        if not number.isnumeric():
            return "Wrong value"
        self.number = number
        return self.number / 100
    
    def square(self, number, exp):
        self.number = number
        self.exp = exp
        result = 'number:' + str(number) + " " + "exp:" + str(exp)
        return str(result)

    def equal(self, text: str):
        # TODO это для переменных для корня
        splitted_string = text.split('(')
        splitted_string2 = splitted_string[1].split(')')
        exp = splitted_string2[0]

        str = text.split(')')
        number = str[1]

        return exp + "," + number


    def pi(self):
        return 3.14

    def exponent(self):
        return 2.72
