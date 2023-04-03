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
        self.number = number
        return self.number / 100
    
    def binary(self, number):
        self.number = number
        if "." in number:
            return "Number is float"
        if int(number) < 0:
            return "Number is < 0"

        number = int(number)
        binaryNum = ""
        while number > 0:
            remainder = number % 2
            binaryNum += str(remainder)
            number //= 2

        number = binaryNum[::-1]
        return number

    def pi(self):
        return 3.14

    def exponent(self):
        return 2.72
