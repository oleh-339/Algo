import unittest

from lab7 import get_max_cars

class TestMaxCars(unittest.TestCase):
    def setUp(self):
        self.path = "test_roads.csv"

    def test_simple_flow(self):
        with open(self.path, "w", encoding="utf-8") as f:
            f.write("F1\nS1\nF1, X1, 10\nX1, S1, 7")
        self.assertEqual(get_max_cars(self.path), 7)

    def test_bottleneck(self):
        with open(self.path, "w", encoding="utf-8") as f:
            f.write("F1, F2\nS1\nF1, X1, 10\nF2, X1, 10\nX1, S1, 12")
        self.assertEqual(get_max_cars(self.path), 12)

if __name__ == "__main__":
    unittest.main()