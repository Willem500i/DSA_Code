from BinarySearchTreeMap import BinarySearchTreeMap

def find_min_abs_difference(bst):
    def min_abs_difference_helper(root):
        ''' Returns a tuple (min, max, min_diff)'''
        if root is None: return (float('inf'),float('-inf'),float('inf'))

        left = min_abs_difference_helper(root.left)
        right = min_abs_difference_helper(root.right)

        minimum_val = min(root.item.key,left[0],right[0])
        maximum_val = max(root.item.key, left[1],right[1])

        min_diff_left = abs(root.item.key - left[1])
        min_diff_right = abs(root.item.key - right[0])
        
        min_diff = min(left[2],right[2],min_diff_left,min_diff_right)

        return (minimum_val,maximum_val,min_diff)

    return min_abs_difference_helper(bst.root)[2]

# bst = BinarySearchTreeMap()
# bst[9] = None
# bst[7] = None
# bst[20] = None
# bst[4] = None
# bst[1] = None
# bst[6] = None
# bst[17] = None
# bst[25] = None
# print([x for x in bst])
# print(find_min_abs_difference(bst))