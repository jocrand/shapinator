class Rectangle:
    """class Rectangle defines a square shape
    Atrributes: width:float, height:float
    Methods: change_width(), change_height(), calculate_perimeter(), calculate_area"""

    def __init__(self, width = 1.0, height = 1.0):
        self.width = width
        self.height = height

    def change_width(self, width):
        self.width = width

    def change_height(self, height):
        self.height = height

    def calculate_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def calculate_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle: width {self.width}, height {self.height}"