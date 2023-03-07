import copy
import numpy as np
from PBox import PBox
import matplotlib.pyplot as plt

"""
Acts as a space to store boxes on an width by height grid.
"""
class Space:

    # initializes the space
    def __init__(self, height, width):
        self.height = int(height)  # height of the space
        self.width = int(width)  # width of the space
        self.boxes = {}  # Dictionary containing the boxes inside the space, with box id as the keys

    # Returns the area of the grid that still empty
    @property
    def area(self):
        return self.height * self.width - np.count_nonzero(self.occ)

    # Bool Array that acts as the space for collision testing
    @property
    def occ(self):
        # If no boxes have been placed return default array
        if len(self.boxes) == 0:
            grid = np.zeros((self.height, self.width), dtype=bool)
        # Otherwise, return the combined occlusion array
        else:
            grid = np.add.reduce([box.occ for box in self.boxes.values()], dtype=bool)
        return grid

    # int Array that acts as the space for collision testing
    @property
    def grid(self):
        grid = np.zeros((self.height, self.width), dtype=int)
        for i, b in self.boxes.items():
            grid += b.occ * i

        return grid


    # Places a given box at the given location, returns true if it is successfully placed, otherwise returns fals
    # If the same box is placed twice, overrides it.
    def place(self, box, y, x):


        # Checks if the box fits
        if (not self.boxFits(box, y, x)):
            return False

        if box.id in self.boxes:
            pBox = self.boxes[box.id]
        else:
            pBox = PBox(box.id, box.height, box.width)

        occ = np.zeros((self.height,self.width), dtype= bool)

        # Adds the box id to the given area
        occ[y:y + box.height, x:x + box.width].fill(True)

        pBox.y = y
        pBox.x = x
        pBox.occ = occ

        # Adds the box to the boxes dictionary
        self.boxes[box.id] = pBox

        # Box successfully placed
        return True



    # Tests if a given box object fits at the given coordinates
    def boxFits(self, box, y, x):
        # Makes sure the that x and y are within bounds
        assert (0 <= y < self.height), "Out of bounds"
        assert (0 <= x < self.width), "Out of bounds"

        # Ensures that there's enough room for the box given it's size.
        if self.height < box.height + y:
            return False
        elif self.width < box.width + x:
            return False


        # slices the sub array that the box would be placed in
        boxArea = self.occ[y:y+box.height,x:x+box.width]

        # Checks if the box would overlap another by checking if Area contains anything other than zeros
        if np.any(boxArea):
            return False

        return True

    # Display the grid as a plot
    def show(self):
        plt.imshow(self.grid, interpolation="nearest")

        # Labels every cell
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                text = plt.text(x, y, self.grid[y, x],
                                ha="center", va="center", color="w")

        plt.show()

    # Returns the number of boxes packed
    def __len__(self):
        return len(self.boxes)

    # Creates a deep copy
    def __deepcopy__(self, memo):
        cls = self.__class__
        cp = cls.__new__(cls)
        memo[id(self)] = cp
        cp.height = self.height
        cp.width = self.width
        cp.boxes = copy.deepcopy(self.boxes)
        return cp

    def __str__(self):
        return str(self.grid) + "\n\n" + str(self.boxes)

    def __repr__(self):
        return str(self)




