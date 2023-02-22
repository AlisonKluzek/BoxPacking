import random as rand
import unittest
from Box import Box
from Space import Space
import main

# Tests the space and box objects
class MyTestCase(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.seed = rand.randint(0,1000000)
        self.seed = 533462
        rand.seed(self.seed)

    # Creates a 5x4 space and a 3x2 box to test with
    def setUp(self):
        self.crate = Space(5, 4)

        self.b1 = Box(1, 3, 2)
        self.b2 = Box(2, 1, 1)
        self.b3 = Box(42, 5, 1)

        self.packer = main.largestFirstPacking


    # Tests if boxFits raises an exception when checking if a box could fit outside the bounds of the space
    def test_boxFits_bounds(self):
        with self.assertRaises(Exception):
            print(self.crate.boxFits(self.b1, 1, 4))
        with self.assertRaises(Exception):
            print(self.crate.boxFits(self.b1, -1, -1))

    # Tests if boxFits acts appropriately when at checking if boxes fit in an empty space, and on the edge of the space
    def test_boxFits_edge(self):
        self.assertEqual(True, self.crate.boxFits(self.b1, 0, 0))
        self.assertEqual(True, self.crate.boxFits(self.b1, 2, 2))
        self.assertEqual(False, self.crate.boxFits(self.b1, 4, 3))

    # Tests if boxFits handles overlap appropriately.
    def test_boxFits_overlap(self):
        self.assertEqual(True, self.crate.boxFits(self.b1, 0, 0))
        self.crate.grid[0,0] = 1
        self.assertEqual(False, self.crate.boxFits(self.b1, 0, 0))
        self.crate.grid[0, 0] = 0

    # TODO add tests for space.place()

    # Tests duplicate place id
    def test_place_id(self):
        with self.assertRaises(Exception):
            self.crate.place(self.b1, 0, 0)
            self.crate.place(self.b1, 2, 2)

    def test_place_overlap(self):
        self.assertEqual(True, self.crate.place(self.b1, 2, 2))
        self.assertEqual(False, self.crate.place(self.b2, 2, 2))
        self.assertEqual(False, self.crate.place(self.b3, 0, 3))
        self.assertEqual(True, self.crate.place(self.b3, 0, 0))
        self.assertEqual(False, self.crate.place(self.b2, 4, 3))
        self.assertEqual(True, self.crate.place(self.b2, 2, 1))
        #print(self.crate.grid)

    # Creates a few random problems to solve
    def test_random_solve(self):
        print(self.seed)
        for i in range(6):

            space = Space(rand.randint(2, 6), rand.randint(2, 6))
            boxes1 = []

            for b in range(rand.randint(5, 10)):
                boxes1.append(Box(b, rand.randint(1, 6), rand.randint(1, 6)))


            c = self.packer(space, boxes1)

            print(c)





if __name__ == '__main__':
    unittest.main()
