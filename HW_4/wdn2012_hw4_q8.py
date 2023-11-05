def flat_list(nested_lst, low, high):
    if low == high:
        if isinstance(nested_lst[low], int):
            return [nested_lst[low]]
        else:
            return flat_list(nested_lst[low], 0, len(nested_lst[low])-1)
    else:
        if isinstance(nested_lst[low], int):
            start = [nested_lst[low]]
        else:
            start = flat_list(nested_lst[low], 0, len(nested_lst[low])-1)
        end = flat_list(nested_lst, low + 1, high)
        return start + end

# nested_lst = [[1, 2], [100,100,3], [4, [5, 6, [7], 8]],[9,[10],[11,12,13]]]
# a = flat_list(nested_lst, 0, 3)
# print(a)
