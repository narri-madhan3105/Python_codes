class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car += 1
    def full_name(self):
        return f"{self.brand} {self.model}"

#everytime u make an object and call the class def init through object total cars will increment
my_brezza=Car("Tata","Beenz")  
my_car=Car("Toyota","Safari")  
driving_car=Car("suzuki","brezza")
print(Car.total_car)
#always access total cars through class not thru objects
#also if you use a class ina another then also it will be counted like the electric car using car's init