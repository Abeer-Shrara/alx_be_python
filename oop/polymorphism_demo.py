# polymorphism_demo.py

import math

class Shape:
    def area(self):
        # meant to be overriden
        raise NotImplementedError("Subclasses must override the area method.")
    
class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    def area(self):
        return self.lenght * self.width

class Circle(Shape):  
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)    