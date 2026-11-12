import math   # using math.pi for calculations

class Circle:
    """class Circle defines a circle shape
    Atrributes: radius:float
    Methods: change_radius(), calculate_circumference(), calculate_area()"""

    def __init__(self, radius = 1.0):
        self.radius = radius

    def change_radius(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle: radius: {self.radius}"