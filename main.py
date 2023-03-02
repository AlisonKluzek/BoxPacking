import copy
import numpy as np
from Box import Box
from Space import Space
from operator import attrgetter
import sys

# Attempts find the best solution to pack Space via brute force
def bruteForcePacking(space, boxes):
    bestSpace = copy.deepcopy(space)    # Best space we've found

    # Base cases
    if np.all(space.grid):      # If grid full
        return bestSpace
    elif not boxes:             # If no boxes left to place
        return bestSpace

    b = boxes[0]            # b is the first box in boxes, we will try to place this box

    # For every spot in space that box b could fit try to place b
    for y in range(space.height - b.height +1):
        for x in range(space.width - b.width +1):
            # Temp copy of space that we can play with
            s = copy.deepcopy(space)

            # If b can be place, place it
            if s.place(b, y, x):

                # Recurse
                s = bruteForcePacking(copy.deepcopy(s), boxes[1:].copy())

            # If we've found a better solution, use it
            if len(s) > len(bestSpace):
                bestSpace = s


    s = bruteForcePacking(copy.deepcopy(space), boxes[1:].copy())
    if len(s) > len(bestSpace):
        bestSpace = s

    return bestSpace

# Sorts the boxes by size, and places the largest boxes first
def largestFirstPacking(space, boxes):
    bestSpace = copy.deepcopy(space)  # Best space we've found

    # Sorts boxes by total area
    boxes = sorted(boxes, key=attrgetter('area'), reverse=True)

    # For every box
    for b in boxes:
        looping = True # Should the loop be ended
        # For every spot in space that box b could fit try to place b
        for y in range(space.height - b.height + 1):
            for x in range(space.width - b.width + 1):
                if looping:
                    if bestSpace.place(b, y, x):
                        looping = False
    return bestSpace

# Sorts the boxes by height, and places the largest boxes first
def tallestFirstPacking(space, boxes):
    bestSpace = copy.deepcopy(space)  # Best space we've found

    # Sorts boxes by height
    boxes = sorted(boxes, key=attrgetter('height'), reverse=True)

    # For every box
    for b in boxes:
        looping = True # Should the loop be ended
        # For every spot in space that box b could fit try to place b
        for y in range(space.height - b.height + 1):
            for x in range(space.width - b.width + 1):
                if looping:
                    if bestSpace.place(b, y, x):
                        looping = False
    return bestSpace

# Loads a space and box list from txt file
def loadCase(file_name):
    f = open(file_name)
    space = None
    boxes = []

    # Creates the space with given dimensions
    w, h = next(f).split()
    space = Space(h, w)

    # Fills boxes with the correct box sizes
    for n in range(int(next(f))):
        l, w, h = next(f).split()
        boxes.append(Box(n, h, w))

    return space, boxes


# TODO this code is a mess right now, will clean up later
if __name__ == '__main__':
    s, b = loadCase("Data/case4.txt")
    print(s)
    print(b)
    np.set_printoptions(threshold=sys.maxsize)

    s = tallestFirstPacking(s,b)

    print(s)

    space = Space(5,4)

    b1 = Box(1, 3, 2)
    b2 = Box(2, 1, 1)
    b3 = Box(3, 2, 2)
    b4 = Box(4, 3, 1)
    b5 = Box(5, 5, 1)
    b6 = Box(6, 1, 4)
    b7 = Box(7, 1, 1)

    boxes = [b1, b2, b3, b4, b5, b6, b7]

    #print(bruteForcePacking(Space(2,2), [Box(1, 1, 1),Box(2,1,1)]))


    #print(bruteForcePacking(space, boxes))


    #print(largestFirstPacking(space, boxes))

    # a = np.arange(20).reshape(5, 4)
    # print(a)
    # print(a[1:2,2:3])
    # print(a[2:5, 2:4])
    # s = a[2:5, 2:4]
    # print(s)
    # #s = crate.grid[2:5, 2:4]
    # s += 10
    # print(s)
    # print(a)
    # #print(np.any(s))
    #
    # c = copy.deepcopy(crate)
    # crate.place(b1, 0, 0)
    # c.place(b1, 0, 0)
    # print(crate)
    # print(c)



