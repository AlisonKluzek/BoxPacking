
"""
A rectangular box, with a width, height and integer id.
"""

class Box:

    # initializes the box
    def __init__(self, id, height = 1, width = 1):
        self.height = height
        self.width = width
        self.id = id

    # TODO add a method to flip the box
