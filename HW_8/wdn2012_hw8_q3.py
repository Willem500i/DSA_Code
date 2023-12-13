from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    '''creates and returns the binary search tree that when
    scanned in prefix order, it would give prefix_lst.'''
    ''' 
    [9, 7, 3, 1, 5, 13, 11, 15]
    insert 9
    add to bst [7, 3, 1, 5, 13, 11, 15] (1,7)

    mid = 5
    insert 7 (left)
    insert 13 (mid)
    add to bst (2,4) [3, 1, 5]

        mid = 4
        insert 3 (left)
        insert 5 (right)
        add to bst (3,3)
            insert 1
        add to bst (5,4)
            return
    
    add to bst (6, 7)
        mid = 7
        insert 11
        insert 15
        add to bst (7,6)
            return
        add to bst (8,7)
            return

    '''
    
    def add_to_bst(bst, prefix_lst, low, high):
        if low > high:
            return
        if low == high:
            bst.insert(prefix_lst[high],None)
        else:
            mid = high
            for i in range(low,high+1):
                if prefix_lst[i] > prefix_lst[low]:
                    mid = i
                    break

            bst.insert(prefix_lst[low],None)
            if prefix_lst[mid] > prefix_lst[low]: bst.insert(prefix_lst[mid],None)

            add_to_bst(bst,prefix_lst,low+1,mid-1)
            if prefix_lst[mid] < prefix_lst[low]: 
                add_to_bst(bst,prefix_lst,mid,high)
            else:
                add_to_bst(bst,prefix_lst,mid+1,high)

    bst = BinarySearchTreeMap()
    if len(prefix_lst) == 0:
        return bst
    bst.insert(prefix_lst[0],None)
    add_to_bst(bst,prefix_lst,1,len(prefix_lst)-1)
    return bst