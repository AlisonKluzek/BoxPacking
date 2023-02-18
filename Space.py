import numpy as np
"""
Acts as a space to store boxes on an width by height grid.
"""
class Space:

    # initializes the space
    def __init__(self, height, width):
        self.height = height  # height of the space
        self.width = width  # width of the space
        self.grid = np.zeros((height, width))  # Int Array that acts as the space
        self.boxes = {}  # Dictionary containing the boxes inside the space, with box id as the keys

    # Places a given box at the given location, returns true if it is successfully placed, otherwise returns false
    # TODO implment
    def place(self, box, y, x):

        # Errors if the same box id is added twice
        assert (box.id not in self.boxes), "That ID is already used"

        # Checks if the box fits
        if (not self.boxFits(box, y, x)):
            return False

        # Adds the box id to the given area
        boxArea = self.grid[y:y + box.height, x:x + box.width]
        boxArea += box.id

        # Adds the box to the boxes dictionary
        self.boxes[box.id] = box

        # Box successfully placed
        return True



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
        boxArea = self.grid[y:y+box.height,x:x+box.width]

        #print((y,y+box.height,x,x+box.width))
        #print(self.grid)
        #print(area)

        # Checks if the box would overlap another by checking if Area contains anything other than zeros
        if np.any(boxArea):
            return False

        return True




