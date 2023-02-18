import numpy as np
from Box import Box
from Space import Space


# TODO this code is a mess right now, will clean up later
if __name__ == '__main__':
    crate = Space(5,4)

    b1 = Box(1, 3, 2)
    b2 = Box(2, 1, 1)
    b3 = Box(3, 2, 2)
    b4 = Box(4, 3, 1)
    b5 = Box(5, 5, 1)
    b6 = Box(6, 1, 1)

    boxs = [b1, b2, b3, b4, b5, b6]

    a = np.arange(20).reshape(5, 4)
    print(a)
    print(a[1:2,2:3])
    print(a[2:5, 2:4])
    s = a[2:5, 2:4]
    print(s)
    #s = crate.grid[2:5, 2:4]
    s += 10
    print(s)
    print(a)
    #print(np.any(s))

