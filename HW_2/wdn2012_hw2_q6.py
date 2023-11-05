def two_sum(srt_lst, target): # theta(n)
    '''
    srt_lst - a list of integers arranged in a sorted order
    target - an integer
    returns two indices (collected in a tuple), such that the elements in their positions add up to target. 
    If there are no such indices, the function should return None.
    '''
    ret = None
    left = 0
    right = len(srt_lst) - 1
    while ret == None and left <= right:
        if srt_lst[left] + srt_lst[right] == target:
            ret = (left, right)
        elif srt_lst[left] + srt_lst[right] > target:
            right = right - 1
        else: # if srt_lst[left] + srt_lst[right] < target
            left = left + 1
    return ret