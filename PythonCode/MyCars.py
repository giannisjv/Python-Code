class car:
    def __init__(self, brand, model, year_of_production):
        self.brand = brand
        self.model = model
        self.year_of_production = year_of_production

    def __str__(self):
        return(f"Your car produced by {self.brand}, the model is {self.model}, and was produced at year {self.year_of_production}")

class  mileage(car):
    def __init__(self, brand, model, year_of_production, service):
        super().__init__(brand, model, year_of_production)
        self.service = service
    def welcome(self):
        print("Your  have to service your car", self.brand, self.model, "at", self.service, "Km")
        print("Your car is ", 2023 - self.year_of_production, "Years old")

class voltage(mileage):
    pass

Car1 = mileage("Reault", "Megane", 2004, 244456)
#print(Car1.service)
Car1.welcome()
print(Car1)