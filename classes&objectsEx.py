# A class a blueprint
# an object is an instance of a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car('Toyota', 'Corolla')
print(my_car.brand)