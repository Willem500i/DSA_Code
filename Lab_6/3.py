def find_max(lst, low, high):
    if low == high:
        return lst[low]
    else:
        if lst[high] > lst[low]:
            return find_max(lst, low + 1, high)
        else:
            return find_max(lst, low, high - 1)
            
print(find_max([0,1,2,3,4,5,100,6,7,8,10],0,4))