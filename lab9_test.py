import unittest
from lab9 import Trie, build_trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = build_trie(["apple", "app", "bat", "ball"])

    def test_search_existing_word(self):
        self.assertTrue(self.trie.search("apple"))

    def test_search_nonexistent_word(self):
        self.assertFalse(self.trie.search("orange"))

    def test_search_prefix_is_not_word(self):
        self.assertFalse(self.trie.search("ap"))

    def test_starts_with_existing_prefix(self):
        self.assertTrue(self.trie.starts_with("ap"))

    def test_starts_with_nonexistent_prefix(self):
        self.assertFalse(self.trie.starts_with("xyz"))

    def test_build_trie_returns_trie_instance(self):
        trie = build_trie(["hello", "world"])
        self.assertIsInstance(trie, Trie)

    def test_insert_and_search_new_word(self):
        self.trie.insert("cat")
        self.assertTrue(self.trie.search("cat"))


if __name__ == "__main__":
    unittest.main()
