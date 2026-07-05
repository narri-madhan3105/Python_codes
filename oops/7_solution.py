#A static method is a function defined inside a class that belongs to the class itself rather than any specific object instance created from that class
#should be accessed using only Car.()
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    @staticmethod
    def general_description():
        return "Cars are means of transport"

my_car=Car("Toyota","Safari")  
print(Car.general_description())
# there should be no self in gen description () while accessing for Car
#self needed only when linking object and class