# inheritance = allows a class to inherit attributes and methods from another class
#             helps with code reusability
#             class Child(parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Micky")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

dog.speak()