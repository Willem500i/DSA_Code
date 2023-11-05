def split_parity(lst): # theta(n)
    odd_index = 0
    for i in range(len(lst)):
        if lst[i-odd_index] % 2 == 0:
            lst[i-odd_index], lst[len(lst)-1-odd_index] =  lst[len(lst)-1-odd_index],lst[i-odd_index]
            odd_index += 1


# lst = [0,14,1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]
# split_parity(lst)
# print(lst)