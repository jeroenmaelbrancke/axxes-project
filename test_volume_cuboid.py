import unittest
from volume_cuboid import *

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1),1)
        # Comment below assertion
        self.assertAlmostEqual(cuboid_volume(0),1)
        self.assertAlmostEqual(cuboid_volume(5.5),166.375)
