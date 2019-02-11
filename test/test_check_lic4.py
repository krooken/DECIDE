import unittest
import decide
from decide import decide
import numpy as np

class CheckLic4TestCase(unittest.TestCase):

    def setUp(self):

        self.points = np.array([(0.0,0.0), (1.0,0.0), (2.0,0.0)])
        self.parameters = {'q_pts': 2, 'quads': 1}

    def run_function(self):

        self.create_points()
        self.lics = decide.LaunchInterceptionConditions(self._points,self.parameters)
        self.result = self.lics.check_lic4()

    def create_points(self):

        self._points = np.array([decide.Point(p) for p in self.points])

    def test_one_quadrant(self):
        # Test that with default input, there is no launch from LIC4 when all points are in one quadrant
        self.points = np.array([(0.0,0.0), (1.0,0.0), (11.0,1.0)])

        self.run_function()
        self.assertFalse(self.result)

    def test_two_quadrants(self):
        # Test that with default input, LIC4 is met.
        self.points = np.array([(0.0,0.0), (1.0,0.0), (-1.0,1.0)])

        self.run_function()
        self.assertTrue(self.result)
