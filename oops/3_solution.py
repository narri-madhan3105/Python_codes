class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car): #inherited car class to electric
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        #car wale class se methods idhar laaya
        self.battery_size = battery_size
my_tesla=ElectricCar("Tesla","Model S","85 KwH")
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.full_name())
#it has access to all attributes, methods

#try this def in Electric car
#def full_name(self):
 #       return f"{self.brand} {self.model} {self.batterysze}"
