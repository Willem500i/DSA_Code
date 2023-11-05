def split_by_sign(lst, low, high):
    if low == high:
        return
    else:
        if lst[low] < 0:
            split_by_sign(lst, low + 1, high)
        elif lst[high] > 0:
            split_by_sign(lst, low, high - 1)
        else:
            lst[low], lst[high] = lst[high], lst[low]
            split_by_sign(lst, low + 1, high)

# lst1 = [1, -1, 2, 4, 6, -6, -7]
# lst2 = [1, 1, 3]
# split_by_sign(lst1, 0, len(lst1) - 1)
# split_by_sign(lst1, 2, len(lst1) - 1)
# split_by_sign(lst2, 2, len(lst2) - 1)
# print(lst1)
# print(lst2)