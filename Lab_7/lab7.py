# 1
def SortLst(lst):
    i = 0
    while i < len(lst):
        if lst[i] != i:
            tmp = lst[i]
            lst[i], lst[tmp] = lst[tmp], lst[i]
        else:
            i += 1
# 2
def intersectionOfLst(lst1,lst2):
    ret = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            ret.append(lst1[i])
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            i += 1
        else:
            j += 1
    return ret

# 3
def isPowerOfTwo(n):
    if n == 1: # got down there evenly
        return True
    elif n < 1: # got down there unevenly
        return False
    return isPowerOfTwo(n/2)

# 4
def split_parity(lst, low, high):
    if low >= high:
        return
    else:
        if lst[low] % 2 == 0:
            split_parity(lst, low + 1, high)
        elif lst[high] % 2 == 1:
            split_parity(lst, low, high-1)
        else:
            lst[low], lst[high] = lst[high], lst[low]
            split_parity(lst, low, high)

# 5
def nested_sum(lst):
    if isinstance(lst, int):
        return lst
    else:
        tot = 0
        for elem in lst:
            tot += nested_sum(elem)
        return tot