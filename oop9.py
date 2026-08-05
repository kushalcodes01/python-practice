class Vehicle:

    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

class car(Vehicle):

    def __init__(self, brand, year,fuel_type):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

c1 = car("Ferari", 1990, "disel")

print(c1.brand)
print(c1.year)
print(c1.fuel_type)
