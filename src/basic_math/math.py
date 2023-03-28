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
        
    def procent(self):
        return self.number / 100
    
    def binary(self):
        binaryRep = ""

        while self > 0:
            remainder = self % 2
            binaryRep += str(remainder)
            self //= 2

        binaryRep = self[::-1]

        return binaryRep
    
    def pi():
        return 3.14
    
    def exponent(): 
        return 2.71