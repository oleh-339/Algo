import unittest
from lab3 import BinaryTree, binary_tree_diameter


class TestTree(unittest.TestCase):
    def test(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.right.right = BinaryTree(5)
        root.left.left.left.left = BinaryTree(9)
        root.left.right.right.right = BinaryTree(6)
        
        result = binary_tree_diameter(root)
        self.assertEqual(result, 6)

    def test_task_example(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        
        result = binary_tree_diameter(root)
        self.assertEqual(result, 2)

    def test_one_node(self):
        root = BinaryTree(10)
        
        result = binary_tree_diameter(root)
        self.assertEqual(result, 0)

    def test_empty(self):
        result = binary_tree_diameter(None)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
