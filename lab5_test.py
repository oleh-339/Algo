import unittest
from lab5 import count_islands

class TestCountIslands(unittest.TestCase):

    def test_example_from_lab_image(self):
        matrix = [
            [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
            [0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
        ]
        self.assertEqual(count_islands(matrix), 5)

    def test_no_islands(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(count_islands(matrix), 0)

    def test_empty_matrix(self):
        self.assertEqual(count_islands([]), 0)

if __name__ == '__main__':
    unittest.main()