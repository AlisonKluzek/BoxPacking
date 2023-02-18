import numpy as np
from Box import Box
from Space import Space

#TODO this code is a mess right now, will clean up later
if __name__ == '__main__':
    crate = Space(5,4)

    b1 = Box(1,3,2)

    a = np.arange(20).reshape(5, 4)
    print(a)
    print(a[1:2,2:3])
    print(a[2:5, 2:4])
    s = a[2:5, 2:4]
    print(type(s))
    s = crate.grid[2:5, 2:4]
    print(np.any(s))

