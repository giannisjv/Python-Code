class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num2 + self.num1
    def minus(self):
        return self.num1 - self.num2
    def multiplication(self):
        return self.num1 * self.num2
    def division(self):
        if (self.num2 != 0):
            return self.num1 / self.num2
        else:
            print("error 15236, you cannot divide with 0 you moron!!!")
    def modulo(self):
        if (self.num2 != 0):
            return self.num1 % self.num2
        else:
            print("error 15236, you cannot divide with 0 you moron!!!")
    
numbers = Calculator(520, 680)
print(numbers.add())
print(numbers.minus())
print(numbers.multiplication())
print(numbers.division())
print(numbers.modulo())


numbe = Calculator(520, 0)
print(numbe.add())
print(numbe.minus())
print(numbe.multiplication())
print(numbe.division())
print(numbe.modulo())

