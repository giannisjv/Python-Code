from datetime import date
class Person:
    def __init__(self, name, country, bdate):
        self.name = name
        self.country = country
        self.bdate = bdate

    def how_old(self):
        today = date.today()
        age = today.year - self.bdate.year
        if (today < date(today.year, self.bdate.month, self.bdate.day)):
            age -= 1
        return age
    
    def person_view(self):
        return f"Your name is {self.name} you are from {self.country} and you are {self.how_old()}"

obj1 = Person("Giannis", "Greece", date(1993, 8, 22))
print(obj1.person_view())
    
