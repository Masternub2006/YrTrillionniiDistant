import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(calculate_average([]))
    def test_positive_numbers(self):
        self.assertEqual(calculate_average([1, 2, 3]), 2.0)
    def test_negative_numbers(self):
        self.assertEqual(calculate_average([-1, -2, -3]), -2.0)
    def test_mixed_numbers(self):
        self.assertEqual(calculate_average([-1, 2, -3, 4]), 0.5)