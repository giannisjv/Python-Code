class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def printme(self):
        print(f"hello for above your class has as a {self.a} and for b {self.b}")

    def add(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def modulo(self):
        return self.a % self.b

class circleArea(calculator):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def Area(self):
        from math import pi
        myNum = calculator(self.a, self.b)
        return myNum.add() **2 * pi

class power(calculator):
    def __init__(self, a, b):
        super().__init__(a, b)
    def mypow(self):
        myNum = calculator(self.a, self.b)
        powe = 1
        for i in range(self.b):
            powe = powe * self.a
        return powe

class pythagorean(calculator):
    def __init__(self, a, b):
        super().__init__(a, b)
    def pyth(self):
        from math import sqrt
        A = power(self.a, 2)
        A = A.mypow()
        B = power(self.b, 2)
        B = B.mypow()
        myNum = calculator(A, B)
        return sqrt(myNum.add())

exit = "n"
mylist = list()
x = "a"
while(exit != "y"):
    while(x != "="):
        x = input("")
        mylist.append(x)
    for i in range(len(mylist)):
        if(mylist[i] == "+"):
            myNum = calculator(int(mylist[i - 1]), int(mylist[i + 1]))
            num = myNum.add()

    print(num)
    exit = "y"

    

"""
myNum = calculator(10, 5)
myNum.printme()
print(myNum.add())
print(myNum.minus())
print(myNum.mult())
print(myNum.div())
print(myNum.modulo())

print("Circle Area")
area = circleArea(10, 15)
print(area.Area())

print("Power")
MyPow = power(2, 4)
print(MyPow.mypow())

print("Pythagorean")
pytha = pythagorean(10, 15)
print(pytha.pyth())

"""