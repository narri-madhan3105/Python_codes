class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    
class ElectricCar(Car): #inherited car class to electric
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
my_tesla=ElectricCar("Tesla","Model S","85 Kw")
                     
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"
class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())