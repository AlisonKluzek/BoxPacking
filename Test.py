import unittest
from Box import Box
from Space import Space

# Tests the space and box objects
class MyTestCase(unittest.TestCase):

    # Creates a 5x4 space and a 3x2 box to test with
    def setUp(self):
        self.crate = Space(5, 4)

        self.b1 = Box(1, 3, 2)
        self.b2 = Box(2, 1, 1)
        self.b3 = Box(42, 5, 1)

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




if __name__ == '__main__':
    unittest.main()
