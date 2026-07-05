#adding a method to give both attributes at once
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
# in class all attributes are accesed with self
my_car=Car("Toyota","Safari")
print(my_car.full_name()) #full_name is a fxn