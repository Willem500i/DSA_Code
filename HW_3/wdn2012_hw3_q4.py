def remove_all(lst, val): # theta(n)
    i,j = 0,0
    
    while i < len(lst): # this loop will always run n times, everything inside runs in theta(1) time
        if lst[i] != val:
            lst[j] = lst[i]
            j += 1
        i += 1

    for k in range(j,i):
        lst.pop()

# lst = [0,1,1,2,3,4,5,1,2,1] # [0,2,3,4,5,2]
# remove_all(lst,1)
# print(lst)