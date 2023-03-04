
"""
A rectangular box, with a width, height and integer id.
"""

class Box:

    # initializes the box
    def __init__(self, id, height = 1, width = 1, y = None, x = None):
        self.height = int(height)
        self.width = int(width)
        self.id = id

    # Returns the total area of the box
    @property
    def area(self):
        return self.width * self.height


    def __add__(self, box):
        return self.area + box.area

    def __str__(self):
        return "{}: {}x{}".format(self.id, self.height, self.width)

    def __repr__(self):
        return str(self)

