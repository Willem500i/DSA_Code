from BinarySearchTreeMap import BinarySearchTreeMap

# a
def create_chain_bst(n):
    '''gets a positive integer n, and returns a binary search 
    tree with n nodes containing the keys 1, 2, 3, ..., n'''
    a = BinarySearchTreeMap()
    for i in range(1,n+1):
        a.insert(i, None)
    return a

# b
def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    midpoint = (low + high) // 2
    bst.insert(midpoint, None)
    if low == high:
        return

    add_items(bst,low,midpoint - 1)
    add_items(bst,midpoint + 1,high)