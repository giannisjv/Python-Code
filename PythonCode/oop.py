class Car:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity}"

    def __str__(self):
        return f"name {self.name}\nmax_speed{self.max_speed}\nmileage{self.mileage}"
    
    def printname(self):
        print(self.name)

class Bus(Car):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)

class limo(Car):
    pass

ModelX = Car("ModelX", 320, 25520)
print(f"max speed {ModelX.max_speed}\nmileage({ModelX.mileage})")
print("\n")
school_Bus = Bus("School Volvo", 180, 2522220)
print(school_Bus)

bus_1 = Bus("road", 120, 35695123)
print("\n\n", bus_1)
print(bus_1.seating_capacity())

x = limo("Mercedes", 180, 35660)
xy = Bus("Volvo",120,15689656)
Car.printname(school_Bus)
x.printname()

print(xy.seating_capacity())