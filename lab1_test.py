import unittest
from lab1 import longest_peak

class TestLongestPeak(unittest.TestCase):

    def test_sorted_up(self):
        numb = [1, 2, 3, 4, 5]
        self.assertEqual(longest_peak(numb), 0)

    def test_sorted_down(self):
        numb = [5, 4, 3, 2, 1]
        self.assertEqual(longest_peak(numb), 0)

    def test_two_el(self):
        numb = [1, 2]
        self.assertEqual(longest_peak(numb), 0)

    def test_no_peak(self):
        numb = [1, 1, 2, 2, 3, 3]
        self.assertEqual(longest_peak(numb), 0)

    def test_three_peaks(self):
        numb = [1, 3, 2, 4, 6, 5, 2, 7, 6]
        self.assertEqual(longest_peak(numb), 5)

if __name__ == "__main__":
    unittest.main()