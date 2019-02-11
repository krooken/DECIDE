import unittest
import decide
from decide import decide

class QuadrantTestCase(unittest.TestCase):

    def test_point_in_first(self):
        # Test a point in the first quadrant

        point = decide.Point((1.0,1.0))
        self.assertEqual(1, point.quadrant())

    def test_point_in_second(self):
        # Test a point in the second quadrant

        point = decide.Point((-1.0,1.0))
        self.assertEqual(2, point.quadrant())

    def test_point_in_third(self):
        # Test a point in third quadrant

        point = decide.Point((-1.0,-1.0))
        self.assertEqual(3, point.quadrant())

    def test_point_in_fourth(self):
        # Test a point in third quadrant

        point = decide.Point((1.0,-1.0))
        self.assertEqual(4, point.quadrant())

    def test_point_between_one_and_four(self):
        # Test a point on the border between one and four
        # The lowest numbered quadrant should be returned

        point = decide.Point((1.0,0.0))
        self.assertEqual(1, point.quadrant())

    def test_point_between_one_and_two(self):
        # Test a point on the border between one and two
        # The lowest numbered quadrant should be returned

        point = decide.Point((0.0,1.0))
        self.assertEqual(1, point.quadrant())

    def test_point_between_two_and_three(self):
        # Test a point on the border between two and three
        # The lowest numbered quadrant should be returned

        point = decide.Point((-1.0,0.0))
        self.assertEqual(2, point.quadrant())

    def test_point_between_three_and_four(self):
        # Test a point on the border between three and four
        # The lowest numbered quadrant should be returned

        point = decide.Point((0.0,-1.0))
        self.assertEqual(3, point.quadrant())

    def test_origin(self):
        # Test that the origin is in the first quadrant.

        point = decide.Point((0.0,0.0))
        self.assertEqual(1, point.quadrant())
