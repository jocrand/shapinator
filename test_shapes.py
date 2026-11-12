"""This is a file where we can test that the classes and their methods work
and make sure certain edge/error cases are handled,
without cluttering our main.py file.

In a large project with many formal tests, you would have multiple test files that live in their own folder."""

import rectangle as rt
import circle as cl

##### TEST OUT THE RECTANGLE CLASS #####
# shape1 = rt.Rectangle()  # test Rectangle object with no args
# print(shape1)
# print(shape1.calculate_perimeter())
    
# shape2 = rt.Rectangle(3.14)  #test Rectangle object with 1 arg
# print(shape2)
# print(shape2.calculate_area())
    
# shape3 = rt.Rectangle(5, 8.0)  #test Rectangle object with 2 args
# print(shape3)
# print(shape3.calculate_area())
# shape3.change_width(2.5)
# shape3.change_height(7.5)
# print(shape3.calculate_area())

# shape4 = rt.Rectangle(-3, -4)   
# print(shape4.calculate_area())   #THIS SHOULDN'T BE ALLOWED, WE NEED TO UPDATE OUR CLASS....

##### TEST OUT THE CIRCLE CLASS #####
sh1 = cl.Circle()  # test Circle with no args
print(sh1)

sh2 = cl.Circle(2.5)  # test Circle with 1 arg
print(sh2)

