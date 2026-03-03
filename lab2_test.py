import unittest
from lab2 import find_distance

class TestCowPlacement(unittest.TestCase):

    def test_example(self):
        n = 5
        c = 3
        sections = [1, 2, 8, 4, 9]
        result = find_distance(n, c, sections)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()