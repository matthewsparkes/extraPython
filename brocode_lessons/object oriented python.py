# object oriented python 

# object = a "bundle" of related attrubutes (variables) and methods (functions)
#          you need a "class" to create many objects.

class Car:
    def __init__(self, model, year, colour, for_sale): # constructor method

        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

car1 = Car("mx5", 2007, "blue", False)
car2 = Car("Cleo", 2008, "purple", True)
car3 = Car("Focus", 2019, "grey", True)

print(car3.model)
print(car3.year)
print(car3.colour)
print(car3.for_sale)


# classes can take up a lot of space, for organisation sake, we can create a new python file within our folder and import it

# methods are actions that our objects can perform

class Car:
    def __init__(self, model, year, colour, for_sale): # constructor method

        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print("You drive the car")

    def stop(self):
        print(f"You stop the {self.colour} {self.model}")

    def describe(self):
        print(f"This car is a {self.year} {self.colour} {self.model}")

car1 = Car("mx5", 2007, "blue", False)
car2 = Car("Cleo", 2008, "purple", True)
car3 = Car("Focus", 2019, "grey", True)

car3.stop()
car1.describe()



# object is a bundle of related attributes
# attributes are variables that an object has
# methods are functions that belong to an object

