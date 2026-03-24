import unittest
from lab4 import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_insert_and_peek(self):
        self.pq.insert("Низький", 1)
        self.pq.insert("Високий", 10)
        self.pq.insert("Середній", 5)
        
        self.assertEqual(self.pq.peek(), ("Високий", 10))

    def test_extract_max(self):
        self.pq.insert("A", 3)
        self.pq.insert("B", 15)
        self.pq.insert("C", 7)
        self.pq.insert("D", 15)
        
        self.assertEqual(self.pq.extract_max()[1], 15)
        self.assertEqual(self.pq.extract_max()[1], 15)
        self.assertEqual(self.pq.extract_max(), ("C", 7))
        self.assertEqual(self.pq.extract_max(), ("A", 3))
        
        self.assertIsNone(self.pq.extract_max())

    def test_empty_queue_peek(self):
        self.assertIsNone(self.pq.peek())

if __name__ == '__main__':
    unittest.main()
