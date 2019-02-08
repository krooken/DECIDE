import unittest
import decide
from decide import decide
import numpy as np
import math

class DecideTestCase(unittest.TestCase):

    def setUp(self):
        # Set up default input data to the function under test in order to reduce the need for copy-pasting and
        # maintenence.
        self.numpoints = 3
        self.points = np.array([(0.0,0.0), (1.0, 0.0), (2.0, 0.0)])
        self.parameters = {
            'length1': 10.0,
            'radius1': 10.0,
            'epsilon': math.pi/2.0,
            'area1': 10.0,
            'q_pts': 2,
            'quads': 1,
            'n_pts': 3,
            'dist': 10.0,
            'k_pts': 1,
            'a_pts': 1,
            'b_pts': 1,
            'c_pts': 1,
            'd_pts': 1,
            'e_pts': 1,
            'f_pts': 1,
            'g_pts': 1,
            'k_pts': 1,
            'length2': 0.0,
            'area2': 1.0
        }
        self.lcm = np.full((15,15), 1)
        self.puv = np.full(15, True)

    def test_negative_decision(self):
        # Test that an input which does not fulfill the conditions will give a negative answer.

        self.run_function()
        self.assertFalse(self.result)

    def test_fuv_bypass(self):
        # Test that setting all values in the PUV (Preliminary Unlocking Vector) to false (i.e. bypass checks) results
        # in a launch decision.

        self.puv = np.full(15, False)

        self.run_function()
        self.assertTrue(self.result)

    def test_lic1_points_apart(self):
        self.points[2] = (11.0, 1.0)
        self.lcm[0,0] = 1
        self.lcm[0,1] = 2
        self.lcm[0,2:] = 3
        self.puv[1:] = False

        self.run_function()

        self.assertTrue(self.result)

    def run_function(self):
        # A helper function that runs the function under test with the indata from the instance variables.
        # The result is stored in an instance variable. This way interface changes are done in one place and not in
        # every test method.

        self.result = decide.decide(self.numpoints, self.points, self.parameters, self.lcm, self.puv)

