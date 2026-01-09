# super() = function used in a child class to call methods from a parent class (superclass)
#           allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()


circle = Circle(colour="red", is_filled=True, radius=5)
square = Square(colour="blue", is_filled=False, width=6)
triangle = Triangle(colour="yellow", is_filled=True, width=7, height=8)

print(triangle.colour)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

triangle.describe()