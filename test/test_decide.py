import unittest
import decide
from decide import decide
import numpy as np
import math

class DecideTestCase(unittest.TestCase):

    def test_negative_decision(self):
        # Test that an input which does not fulfill the conditions will give a negative answer.
        numpoints = 3
        points = np.array([(0.0,0.0), (1.0, 0.0), (2.0, 0.0)])
        parameters = {
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
        lcm = np.full((15,15), 1)
        puv = np.full(15, True)

        self.assertFalse(decide.decide(numpoints, points, parameters, lcm, puv))

    def test_fuv_bypass(self):
        # Test that setting all values in the PUV (Preliminary Unlocking Vector) to false (i.e. bypass checks) results
        # in a launch decision.

        numpoints = 3
        points = np.array([(0.0,0.0), (1.0, 0.0), (2.0, 0.0)])
        parameters = {
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
        lcm = np.full((15,15), 1)
        puv = np.full(15, False)

        self.assertTrue(decide.decide(numpoints, points, parameters, lcm, puv))