# Encapsulation helps in data hiding,,maintainability.
# things are accessible but with privacy
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def get_brand(self):
        return self.__brand + "!"
    
class ElectricCar(Car): #inherited car class to electric
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
my_tesla=ElectricCar("Tesla","Model S","85 KwH")
#two undescores make it private

#print(my_tesla.__brand)
print(my_tesla.get_brand()) #getter method
 #can access it only through get_brand()y


 #know about setter as well