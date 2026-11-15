import math   # using math.pi for calculations
# code to run the user menu and get the user's choice
import subprocess
import time   # for time.sleep() to control timing of display

def display_menu():
    # subprocess.run('clear')
    time.sleep(1)
    print("\n*** SHAPINATOR MENU ***")
    print("1. Add a circle\n\
2. Add a rectangle\n\
3. See my collection\n\
4. End\n")

def get_user_choice():
    choice = input("Please choose 1, 2, 3, or 4\n")
    return choice

###########################################################################3
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

######################################################################################
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

####################################################################################
class Collection:
    """Collection class
    Attributes: shapes:list
    Methods: add_shape(), __str__()"""

    def __init__(self):
        self.shapes = []  #initialized as an empty list

    def add_shape(self, shape):
        self.shapes.append(shape)
        print("Shape successfully added.")

    def display_collection(self):
        if len(self.shapes) > 0:
            print("\nYour shape collection:")
            for shape in self.shapes:
                print(shape)
        else:
            print("\nYour shape collection is empty!\n")