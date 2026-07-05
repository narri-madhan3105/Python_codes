class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"
class Ecar(Car):
    def __init__(self,brand,model,batterysze):
        super().__init__(brand,model)
        self.batterysze=batterysze
    def fuel_type(self):
        return "Electric Charge"

my_tesla=Ecar("tesla","suv","585kwh")
print(my_tesla.fuel_type())

my_brezza=Car("Tata","Beenz")
print(my_brezza.fuel_type())
        