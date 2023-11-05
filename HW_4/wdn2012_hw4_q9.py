def permutations(lst, low, high):
    if low == high:
        num = lst[low]
        if isinstance(num, int):
            return [[num]]
        else:
            return [num]
    else:
        perms = permutations(lst, low, high - 1)
        var = lst[high]
        ret = []
        for i in range(high-low+1):
            for perm in perms:
                if isinstance(perm, int):
                    num = [perm]
                else:
                    num = perm.copy()
                num.insert(i,var)
                ret += [num]
        return ret
# a = permutations([1,2,3],0,2)
# print(a)
# i = perms [1] = [1]
# a = perms [1,2] = [[1,2], [2,1]]
# b = perms [1,2,3] = [[1, 2, 3], [2, 1, 3], [1, 3, 2], [3, 2, 1], [3, 1, 2], [2, 3, 1]]

# [3+a[0],  3  + a[1]] add to the start .insert(0,3)
# [a[0].insert(1,3), a[1].insert(1,3)] add to the middle .insert(1,3)
# [a[0]+3, a[1] + 3] add to the end .insert(2,3)
