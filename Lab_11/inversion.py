class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key 
        self.left = left 
        self.right = right
def invert(head):
    if head.left is None:
        return head
    else:
        new_left = invert(head.right)
        new_right = invert(head.left)
        head.left = new_left
        head.right = new_right
        return head
    
def print_tree_inorder(node):
    if node is not None:
        print_tree_inorder(node.left)
        print(node.key, end=" ")
        print_tree_inorder(node.right)

# Create a binary tree:
#          1
#       /    \
#      2      3
#     / \    / \
#    4   5  6   7
root = Node(1, Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))

# Print the original tree
print("Original tree (inorder traversal):")
print_tree_inorder(root)
print("\n")

# Invert the tree
inverted_root = invert(root)

# Create a binary tree:
#         1
#       /    \
#      3      2
#     / \    / \
#    7   6  5   4

# Print the inverted tree
print("Inverted tree (inorder traversal):")
print_tree_inorder(inverted_root)