class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(tree: BinaryTree) -> int:
    def my_max(a: int, b: int) -> int:
        return a if a > b else b

    def dfs(node: BinaryTree):
        if node is None:
            return 0, 0

        left_height, left_diam = dfs(node.left)
        right_height, right_diam = dfs(node.right)

        current_diam = left_height + right_height
        max_child_diam = my_max(left_diam, right_diam)
        max_diam = my_max(max_child_diam, current_diam)

        current_height = my_max(left_height, right_height) + 1

        return current_height, max_diam

    _, final_diameter = dfs(tree)
    return final_diameter
