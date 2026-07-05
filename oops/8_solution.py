class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model
    @property
    def model(self):
        return self.__model
#you dont need strivtly need to make it private But this breaks — infinite recursionv
my_car=Car("Toyota","Safari")
print(my_car.model)
my_car.model="Alto"
#Using @model.setter you can change the private variable value, but in a controlled way

