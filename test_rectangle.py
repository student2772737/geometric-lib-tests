import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        result = area(3, 4)
        self.assertEqual(result, 12)
    def test_area_first_zero(self):
        result = area(0, 10)
        self.assertEqual(result, 0)
    def test_area_second_zero(self):
        result = area(10, 0)
        self.assertEqual(result, 0)
    def test_area_float1(self):
        result = area(2.5, 4)
        self.assertAlmostEqual(result, 10)
    def test_area_float2(self):
        result = area(3, 1.5)
        self.assertAlmostEqual(result, 4.5)
    def test_area_close_to_zero(self):
        result = area(0.1, 2)
        self.assertAlmostEqual(result, 0.2)

    def test_perimeter_normal(self):
        result = perimeter(5, 6)
        self.assertEqual(result, 22)
    def test_perimeter_first_zero(self):
        result = perimeter(0, 6)
        self.assertEqual(result, 12)
    def test_perimeter_second_zero(self):
        result = perimeter(5, 0)
        self.assertEqual(result, 10)
    def test_perimeter_float1(self):
        result = perimeter(5.4, 2)
        self.assertAlmostEqual(result, 14.8)
    def test_perimeter_float2(self):
        result = perimeter(4, 3.8)
        self.assertAlmostEqual(result, 15.6)
    def test_perimeter_close_to_zero(self):
        result = perimeter(0.1, 1)
        self.assertAlmostEqual(result, 2.2)

