import unittest
from unittest import TestCase
from main import calculate_lbtt


class InitialTest(TestCase):

    def test_0_percent_value(self):
        self.assertEqual(0, calculate_lbtt(500))

    def test_negative_value(self):
        self.assertRaises(ValueError, calculate_lbtt, -1)

    def test_string_value(self):
        self.assertRaises(TypeError, calculate_lbtt, "Not a float")

    def test_12_percent_value(self):
        self.assertAlmostEqual(97440, calculate_lbtt(812000))

    def test_5_percent_value(self):
        self.assertAlmostEqual(16250, calculate_lbtt(325000))


if __name__ == "__main__":
    unittest.main()