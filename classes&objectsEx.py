# A class a blueprint
# an object is an instance of a class
# A class defines attributes and behaviors. Objects are concrete realization of that definition.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car('Toyota', 'Corolla')
print(my_car.brand)

# __init__ methods and types:
class Example:
    class_var = 'I am a class variable'
    def __init__(self, value):
        self.value= value

    def instance_method(self):
        return f'Instance method: value = {self.value}'

    @classmethod
    def class_method(cls):
        return f'Class Method: class_var = {cls.class_var}'

    @staticmethod
    def static_method():
        return 'Static method: no access to instance or class'

obj = Example(42)
# Key differences:
# Instance methods: Access/modify instance data via self.
# Class methods: Work with the class itself via cls.
# Static methods: Utility functions that don’t need self or cls.
print(obj.instance_method())  #needs object
print(Example.class_method())   #can be called on class
print(Example.static_method())  #utility method
