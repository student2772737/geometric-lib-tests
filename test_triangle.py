import unittest
from triangle import area, perimeter
class TestTriangle(unittest.TestCase):

    def test_area_normal(self):
        result = area(3, 4)
        self.assertAlmostEqual(result, 6.0)
    def test_area_zero2(self):
        result = area(3, 0)
        self.assertEqual(result, 0)
    def test_area_zero1(self):
        result = area(0, 4)
        self.assertEqual(result, 0)
    def test_area_float(self):
        result = area(3.3, 4.1)
        self.assertAlmostEqual(result, 6.765)
    def test_area_close_to_zero(self):
        result = area(0.1, 3)
        self.assertAlmostEqual(result, 0.15)

    def test_perimeter_normal(self):
        result = perimeter(3, 4, 5)
        self.assertEqual(result, 12)
    def test_perimeter_zero(self):
        result = perimeter(3, 4, 0)
        self.assertEqual(result, 7)
    def test_perimeter_float(self):
        result = perimeter(3.1, 4.6, 7.3)
        self.assertAlmostEqual(result, 15.0)
    def test_perimeter_close_to_zero(self):
        result = perimeter(0.1, 0.1, 0.1)
        self.assertAlmostEqual(result, 0.3)

