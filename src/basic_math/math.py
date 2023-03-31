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
        binaryRep = " "
        while number > 0:
            remainder = number % 2
            binaryRep += str(remainder)
            number //= 2

        number = binaryRep[::-1]
        return number

    def pi(self):
        return 3.14

    def exponent(self):
        return 2.72
