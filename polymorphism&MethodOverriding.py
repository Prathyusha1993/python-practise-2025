# polymorphism: The ability of different objects to respond to the same method name in a way specific to their type.

class Animal:
    def speak(self):
        return 'Some Sound'

class Dog(Animal):
    def speak(self):
        return 'Woof!'

class Cat(Animal):
    def speak(self):
        return 'Meow'


animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())


# Polymorphism: Same method name, different behavior depending on the object.
# Method overriding: Child class redefines a parent method.