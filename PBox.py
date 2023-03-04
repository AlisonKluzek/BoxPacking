from Box import Box

"""
A subclass of Box, with positional data and an occlusion map
"""
class PBox(Box):
    def __init__(self, id, height = 1, width = 1, y = None, x = None, occ = None):
        super().__init__(id, height, width)
        self.y = y
        self.x = x
        self.occ = occ


    # Returns a tuple with all the essential data to describe the box
    @property
    def tup(self):
        return (self.y, self.x, self.width, self.height)


    # Flips the box at a 90-degree angle
    def flip(self):
        self.height, self.width = self.width, self.height

    def __add__(self, other):
        return self.occ + other

    def __str__(self):
        return "{}: {}x{}, ({},{})".format(self.id, self.height, self.width, self.y, self.x)