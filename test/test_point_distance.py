import unittest
import decide
from decide import decide

class PointDistanceTestCase(unittest.TestCase):

    def test_vertical_distance(self):
        # Test that a point right above origin gets correct distance

        distance = 4.0

        point1 = (0.0,0.0)
        point2 = (0.0,distance)

        self.assertEqual(distance, decide.point_distance(point1,point2))

    def test_vertical_distance_reverse(self):
        # Test that a point right above origin gets correct distance, when the first point is above

        distance = 4.0

        point1 = (0.0,distance)
        point2 = (0.0,0.0)

        self.assertEqual(distance, decide.point_distance(point1,point2))
