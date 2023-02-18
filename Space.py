import numpy as np
"""
Acts as a space to store boxes on an width by height grid.
"""
class Space:

    # initializes the space
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = np.zeros((height, width))
        self.boxes = {}

    # Places a given box at the given location
    # TODO implment
    def place(self, box, y, x):
        raise NotImplementedError

    # Tests if a given box object fits at the given coordinates
    def boxFits(self, box, y, x):
        # Makes sure the that x and y are within bounds
        assert (0 <= y < self.height), "Out of bounds"
        assert (0 <= x < self.width), "Out of bounds"

        # Ensures that there's enough room for the box given it's size.
        if self.height < box.height + y:
            print(box.height + y)
            return False
        elif self.width < box.width + x:
            return False

        # slices the sub array that the box would be placed in
        area = self.grid[y:y+box.height,x:x+box.width]

        #print((y,y+box.height,x,x+box.width))
        #print(self.grid)
        #print(area)

        # Checks if the box would overlap another by checking if Area contains anything other than zeros
        if np.any(self.grid[y:y+box.height,x:x+box.width]):
            return False

        return True




