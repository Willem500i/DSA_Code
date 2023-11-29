def min_and_max(bin_tree):
    if bin_tree.root is None:
        raise Exception("Empty Tree")
    def subtree_min_and_max(root):
        if root is None:
            return None
        else:
            left = subtree_min_and_max(root.left)
            right = subtree_min_and_max(root.right)
            if left is None and right is None:
                return (root.data,root.data)
            if left is not None and right is not None:
                return (min(left[0],right[0],root.data),max(left[1],right[1],root.data))
            return left if right is None else right

    return subtree_min_and_max(bin_tree.root)

'''
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.data = key 
        self.left = left 
        self.right = right

def subtree_min_and_max(root):
        if root is None:
            return None
        else:
            left = subtree_min_and_max(root.left)
            right = subtree_min_and_max(root.right)
            if left is None and right is None:
                return (root.data,root.data)
            if left is not None and right is not None:
                return (min(left[0],right[0],root.data),max(left[1],right[1],root.data))
            return left if right is None else right

# Create a binary tree:
#          1
#       /    \
#      2      3
#     / \    / \
#    4   10  6   7
root = Node(100, Node(2,Node(4),Node(10)),Node(3,Node(6),Node(7)))

print(subtree_min_and_max(root))
'''