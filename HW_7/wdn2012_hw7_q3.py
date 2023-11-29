def is_height_balanced(bin_tree):
    def subtree_heights(root):
        if root is None:
            return (0,0)
        if root.right is None and root.left is None:
            return (1,0)
        else:
            right = subtree_heights(root.right) # (right_height, right_biggest_diff)
            left = subtree_heights(root.left) # (left_height, left_biggest_diff)
            return (max(right[0],left[0]) + 1, max(right[1],left[1],abs(right[0]-left[0])))
    stats = subtree_heights(bin_tree.root)
    return stats[1] <= 1

'''

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.data = key 
        self.left = left 
        self.right = right

# Create a binary tree:
#         100
#       /    \
#      2      3
#     / \    / \
#    4   10  0   7
#               / \
#               2  5
#                  /\
#                 1  2
root = Node(100, Node(2,Node(4),Node(10)),Node(3,Node(0),Node(7,Node(2),Node(5,Node(1),Node(2)))))

print(is_height_balanced(root))
'''