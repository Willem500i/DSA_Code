def binary_search(lst, low, high, val):
    mid = (low + high) // 2
    if lst[mid] == val:
        return mid
    elif (low >= high):
        return None
    else:
        if lst[mid] < val:
            return binary_search(lst, mid + 1, high, val)
        else:
            return binary_search(lst, low, mid - 1, val)
        
print(binary_search([0,1,2,3,4,5,6,7],0,7,1))