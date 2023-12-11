"""
Helper function display binary search tree maps
"""

# from BinartSearchTreeMap import BinartSearchTreeMap
from BinarySearchTreeMap import BinarySearchTreeMap

# Adapted from https://leetcode.com/discuss/interview-question/1954462/pretty-printing-binary-trees-in-python-for-debugging
def print_bstm(bstm: BinarySearchTreeMap, print_item_value: bool=False):
    """Pretty prints a binary search tree map
    :param print_item_value: whether to print the value of the item in the node or just the key"""
    def _display_aux(node, print_item_value=False):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = f'{node.item.key}{":" + str(node.item.value) if print_item_value else ""}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = _display_aux(node.left, print_item_value)
            s = f'{node.item.key}{":" + str(node.item.value) if print_item_value else ""}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = _display_aux(node.right, print_item_value)
            s = f'{node.item.key}{":" + str(node.item.value) if print_item_value else ""}'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = _display_aux(node.left, print_item_value)
        right, m, q, y = _display_aux(node.right, print_item_value)
        s = f'{node.item.key}{":" + str(node.item.value) if print_item_value else ""}'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    if not bstm.root:
        print("Empty tree. bstm.root is None")
        return
    lines, *_ = _display_aux(bstm.root, print_item_value)
    for line in lines:
        print(line)

if __name__ == "__main__":
    """
    bstm = 
          _5
         /  \
         3  7
          \  \
          4  8
           _____5:25__
          /           \
         3:9__      7:49__
              \           \
            4:16        8:64
    """
    bstm = BinarySearchTreeMap()
    for i in [5, 3, 4, 7, 8]:
        bstm.insert(i, i*i)  # inserts (key, value) pair into the tree
    print_bstm(bstm)
    print_bstm(bstm, True)
