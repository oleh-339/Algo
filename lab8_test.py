import unittest
from lab8 import find_longest_chain

class TestWordChain(unittest.TestCase):
    
    def test_example_1(self):
        words = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        expected_result = 6
        self.assertEqual(find_longest_chain(words), expected_result)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        expected_result = 4
        self.assertEqual(find_longest_chain(words), expected_result)

    def test_example_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        expected_result = 1
        self.assertEqual(find_longest_chain(words), expected_result)
        
    def test_empty_list(self):
        self.assertEqual(find_longest_chain([]), 0)

if __name__ == '__main__':
    unittest.main()