#  Polymorphism and method overriding

import math

class Shape:
    def area(self):
        raise NotImplementedError
# Class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    # The rectangle's area method
    def area(self):
        area_of_rectangle = self.length * self.width
        return area_of_rectangle
# class Circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    # Circle area method
    def area(self):
        area_of_circle = math.pi * (self.radius**2)
        return area_of_circle

    