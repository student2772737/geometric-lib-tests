import unittest
from square import area, perimeter
class SquareTestCase(unittest.TestCase):

    def test_area_normal(self):
        result = area(3)
        self.assertEqual(result, 9)
    def test_area_zero(self):
        result = area(0)
        self.assertEqual(result, 0)
    def test_area_float(self):
        result = area(2.5)
        self.assertAlmostEqual(result, 6.25)
    def test_area_close_to_zero(self):
        result = area(0.1)
        self.assertAlmostEqual(result, 0.01)

    def test_perimeter_normal(self):
        result = perimeter(5)
        self.assertEqual(result, 20)
    def test_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result, 0)
    def test_perimeter_float1(self):
        result = perimeter(5.4)
        self.assertAlmostEqual(result, 21.6)
    def test_perimeter_close_to_zero(self):
        result = perimeter(0.1)
        self.assertAlmostEqual(result, 0.4)

