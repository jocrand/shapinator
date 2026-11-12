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
        

