class Vehicle:
    color = "white"
    def __init__(self,name, max_speed, mileage, capacity, doors):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
        self.doors = doors

    def seating_capacity(self, capacity):
        return f"The Capacity of a {self.name} is {capacity} passengers"
    
    def fare(self):
        amount = self.capacity * 100
        amount += amount *10 / 100
        return amount
    
    def doorNum(self):
        return f"Your {self.name} has {self.doors}"

class MyCar:
    pass 

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity, doors):
        super().__init__(name, max_speed, mileage, capacity, doors)
    
    def seating_capacity(self):
        return super().seating_capacity(self.capacity)

    def fare(self):
        return super().fare()
    
    def doorNum(self):
        return super().doorNum()

class SUV(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity, doors):
        super().__init__(name, max_speed, mileage, capacity, doors)
    
    def doorNum(self):
        return super().doorNum()


Corsa = Vehicle("Corsa", 150, 255220, 4, 5)
print(Corsa.color, Corsa.name, Corsa.max_speed, Corsa.mileage)

Volvo = Bus("Volvo", 150, 365522, 45, 2)
RAV4 = SUV("Volvo", 180, 365862, 5, 3)
print(Volvo.color,"Vehicle Name ", Volvo.name, " Max Speed ", Volvo.max_speed, " Mileage ", Volvo.mileage)
print(Volvo.seating_capacity())
print("Total Bus Fare is: ",Volvo.fare())
print(f"Total fare of {Corsa.name} is {Corsa.fare()}")
print(Volvo.doorNum())
print(Corsa.doorNum())
print(RAV4.doorNum())
print(type(RAV4))
print(type(Corsa))
print(isinstance(RAV4, Vehicle))

