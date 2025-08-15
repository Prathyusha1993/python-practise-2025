# inheritance: the process by which one class acquires the properties and behavior of another class(super/parent class)
# promoting code reuse and hierarchical relationships.

class Animal:
    def speak(self):
        return 'Some Sound'

class Dog(Animal):
    def speak(self):
        return 'Woof!'

class Cat(Animal):
    def speak(self):
        return 'Meow'

animal = Animal()
print(animal.speak())

dog1 = Dog()
print(dog1.speak())

cat1 = Cat()
print(cat1.speak())


# Multiple inheritance:
class Robot:
    def charge(self):
        return 'Charging...'

class RoboDog(Dog, Robot):
    pass

dog = Dog()
print(dog.speak())

robo = RoboDog()
print(robo.speak())
print(robo.charge())