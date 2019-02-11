import unittest
import decide
from decide import decide
import numpy as np

class CheckLic0TestCase(unittest.TestCase):

    def setUp(self):

        self.points = np.array([(0.0,0.0), (1.0,0.0), (2.0,0.0)])
        self.parameters = {'length1': 10.0}

    def run_function(self):

        self.lics = decide.LaunchInterceptionConditions(self.points,self.parameters)
        self.result = self.lics.check_lic0()

    def test_consecutive_points_apart(self):

        self.points = np.array([(0.0,0.0), (1.0,0.0), (11.0,1.0)])

        self.run_function()
        self.assertTrue(self.result)

    def test_non_consecutive_points_apart(self):

        self.points = np.array([(0.0,0.0), (9.0,0.0), (15.0,0.0)])

        self.run_function()
        self.assertFalse(self.result)
