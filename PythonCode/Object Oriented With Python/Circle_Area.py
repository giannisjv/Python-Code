class Circle:
    def __init__(self, a):
        self.a = a
    def area(self):
        import math
        return math.pi * self.a * self.a
    def perimeter(self):
        from math import pi
        return 2 * pi * self.a
    
cir = Circle(10)
print(cir.area(), cir.perimeter())