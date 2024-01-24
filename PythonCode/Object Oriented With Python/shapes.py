import math
class shapes:
    def area(self):
        pass
    def perimeter(self):
        pass
    def __str__(self):
        return f"area {self.area()} perimeter {self.perimeter()}"
class circle(shapes):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius

class reactangle(shapes):
    def __init__(self, length, width):
        self.side1 = length
        self.side2 = width
    def area(self):
        return self.side1 * self.side2
    def perimeter(self):
        return 2 * (self.side1 + self.side2)
    
class triangle(shapes):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
cir = circle(50)
square = reactangle(50, 50)
reactangle1 = reactangle(50,70)
triangle1 = triangle(10,20,10,20,30)
print(cir)
print(square)
print(reactangle1)
print(triangle1)

