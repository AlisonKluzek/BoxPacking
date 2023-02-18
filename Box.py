
"""
A rectangular box, with a width, height and integer id.
"""

class Box:

    # initializes the box
    def __init__(self, id, height = 1, width = 1):
        self.height = height
        self.width = width
        self.id = id

    # Flips the box at a 90-degree angle
    def flip(self):
        self.height, self.width = self.width, self.height

