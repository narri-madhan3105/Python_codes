#to prove my_tesla is an instance of both electric_Car and Car
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    
class ElectricCar(Car): #inherited car class to electric
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
my_tesla=ElectricCar("Tesla","Model S","85 KwH")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))