def findChange(lst01): # Θ(log_2(𝑛))
    # binary search, looking for [0,1]
    left = 0
    right = len(lst01) -1
    mid = (left + right) // 2
    ret = None
    while ret == None and left <= right:
        if lst01[mid-1:mid+1] == [0,1]:
            ret = mid
        elif lst01[mid] == 0:
            left = mid + 1
        else: # lst01[mid] == 1
            right = mid - 1
        mid = (left + right) // 2
    return ret

print(findChange([1,1,1,1]))