from ArrayQueue import *

class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self
            self.parent = None


    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def count_nodes(self):
        def subtree_count(root):
            if(root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return left_count + right_count + 1

        return subtree_count(self.root)
    # 2
    def __contains__(self, item):
        ''' Returns True if val exists in the binary tree and
        false if not'''
        def contains(root):
            if root.data is None:
                return False
            else:
                left = contains(root.left)
                right = contains(root.right)
                return (root.data == item) or left or right
            
        return contains(self.root)

# 1
def bt_even_sum(root):
    ''' Returns the sum of all even integers in the binary
    tree'''
    if root.data is None:
        return 0
    else:
        add = root.data if root.data % 2 == 0 else 0
        return bt_even_sum(root.left) + bt_even_sum(root.right) + add

# 3
def is_full(root):
     ''' Returns True if the Binary Tree is full and false
     if not '''
     if root.data is None:
         return False
     else:
         left = is_full(root.left)
         right = is_full(root.right)
         return (left == right)
     
#4
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        if (left is not None):
            self.left.parent = self
        self.right = right
        if (right is not None):
            self.right.parent = self
        self.parent = None

def merge_bt(root1, root2):
    ''' Creates a new binary tree merging tree1 and tree2
    and returns its root. '''
    if root1.data is None and root2.data is None:
        return None
    if root1.data is None:
        left = merge_bt(root1, root2.left)
        right = merge_bt(root1, root2.right)
        return Node(root2.data,left,right)
    if root2.data is None:
        left = merge_bt(root1.left, root2)
        right = merge_bt(root1.right, root2)
        return Node(root1.data,left,right)
    else:
        left = merge_bt(root1.left, root2.left)
        right = merge_bt(root1.right, root2.right)
        return Node(root1.data + root2.data, left, right)
    
def invert_bt(root):
       ''' Inverts the binary tree using recursion '''
       if root.left is None:
            return root
       else:
            new_left = invert_bt(root.right)
            new_right = invert_bt(root.left)
            root.left = new_left
            root.right = new_right
            return root

def invert_bt(root): # WIP
    ''' Inverts the binary tree without recursion '''
    q = ArrayQueue()
    q.enqueue(root)
    while q:
        curr = q.dequeue()
        if curr.right:
            q.enqueue(curr.right)
        if curr.left:
            q.enqueue(curr.left)
        
        



    


       
