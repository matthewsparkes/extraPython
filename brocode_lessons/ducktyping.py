
# Duck typing = Another way to acheve polymorphism besies using Inheritance
#               Object must have the minim necessary attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):

    def speak(self):
        print("MEOW!")

class Car:
    
    alive = True

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)