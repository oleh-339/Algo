import os

def my_max(a, b):
    return a if a > b else b

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def print_tree(self):
        def get_h(node):
            if not node: return 0
            return my_max(get_h(node.left), get_h(node.right)) + 1
        
        h = get_h(self)
        if h == 0: return
        
        rows = 2 ** h + 1
        cols = 100 
        matrix = [[" " for _ in range(cols)] for _ in range(rows)]
        
        def place(r, c, txt):
            s = str(txt)
            start = c - len(s) // 2
            for i, char in enumerate(s):
                if 0 <= r < rows and 0 <= start + i < cols:
                    matrix[r][start + i] = char

        def draw_line(r1, c1, r2, c2):
            if r1 == r2: 
                mc = (c1 + c2) // 2
                if 0 <= r1 < rows and 0 <= mc < cols:
                    matrix[r1][mc] = "─"
            else: 
                mr = (r1 + r2) // 2
                mc = (c1 + c2) // 2
                if 0 <= mr < rows and 0 <= mc < cols:
                    if (r2 < r1) == (c2 < c1): matrix[mr][mc] = "╲"
                    else: matrix[mr][mc] = "╱" 

        def fill_subtree(node, parent_r, parent_c, top_r, bottom_r, direction, depth):
            if not node: return
            r = (top_r + bottom_r) // 2
            h_offset = my_max(4, 15 // (depth + 1)) 
            c = parent_c + direction * h_offset
            
            draw_line(parent_r, parent_c, r, c)
            place(r, c, node.value)
            
            fill_subtree(node.left, r, c, top_r, r, direction, depth + 1)
            fill_subtree(node.right, r, c, r, bottom_r, direction, depth + 1)

        root_r, root_c = rows // 2, cols // 2
        place(root_r, root_c, self.value)
        
        fill_subtree(self.left, root_r, root_c, 0, rows, -1, 1)
        fill_subtree(self.right, root_r, root_c, 0, rows, 1, 1)
        
        for row in matrix:
            line = "".join(row).rstrip()
            if line: print(line)


def build_level_order(arr):
    if not arr: return None
    root = BinaryTree(arr[0])
    queue = [root] 
    i = 1
    
    while queue and i < len(arr):
        current = queue.pop(0) 
        if i < len(arr):
            if arr[i] is not None:
                current.left = BinaryTree(arr[i], parent=current)
                queue.append(current.left)
            i += 1
        if i < len(arr):
            if arr[i] is not None:
                current.right = BinaryTree(arr[i], parent=current)
                queue.append(current.right)
            i += 1
    return root

def get_inorder(root):
    res = []
    def traverse(node):
        if not node: return
        traverse(node.left)
        res.append(str(node.value))
        traverse(node.right)
        
    traverse(root)
    return res

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "tree.txt")
    
    if not os.path.exists(filename):
        print(f"Помилка: Файл {filename} не знайдено!")
        return

    with open(filename, "r", encoding="utf-8") as file:
        tokens = file.read().split()

    nums = []
    for t in tokens:
        if t.lower() in ('nil', 'n', 'null'):
            nums.append(None)
        else:
            try:
                nums.append(int(t))
            except ValueError:
                pass
                
    if len(nums) > 20:
        nums = nums[:20]

    root = build_level_order(nums)

    if root:
        print("Вигляд дерева зверху:")
        root.print_tree()
        
        in_ord = get_inorder(root)
        print(f"In-order: {' -> '.join(in_ord)}")
    else:
        print("Дерево порожнє")

if __name__ == "__main__":
    main()
