#  Polymorphism and method overriding

import math


class Shape:
    def area(self):
        raise NotImplementedError 
    

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        area_of_rectangle = self.length * self.width
        return area_of_rectangle

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        area_of_circle = math.pi * (self.radius**2)
        return area_of_circle

    