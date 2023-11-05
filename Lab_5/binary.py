def binary_search(lst,val):
    left = 0
    right = len(lst)
    mid = (left + right) // 2
    ret = None
    while ret == None and left <= right:
        if lst[mid] == val:
            ret = mid
        elif lst[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    return ret

'''
Input: nums = [15, 20, 21, 1, 3, 6, 7, 10, 12, 14]
Output: 3
'''
nums = [15, 20, 21, 22,1, 3, 6, 7, 10, 12, 14]
nums_sorted = [1, 3, 6, 7, 10, 12, 14,15, 20, 21]
def find_pivot(lst):
    # find two next to eachother that arent sorted
    left = 0
    right = len(lst)
    mid = (left + right) // 2
    ret = None
    while ret == None and left <= right:
        if lst[mid-1] > lst[mid]:
            ret = mid
        elif lst[mid] < lst[left]:
            right = mid - 1
        else: # lst[mid] > lst[left]
            left = mid + 1
        mid = (left + right) // 2
    return ret

def find_val(lst,val):
    pivot = find_pivot(lst)
    if lst[0] > val:
        return binary_search(lst[pivot:len(lst)],val) + pivot
    else:
        return binary_search(lst[0:pivot],val)