from ArrayQueue import *

def flatten_list_by_depth(lst): 
    """
    : lst type: list
    : return type: list """
    q = ArrayQueue() 
    new_lst = []
    still_going = True

    for i in range(len(lst)):
        q.enqueue(lst[i])
    
    while q:
        elem = q.dequeue()
        if type(elem) == int:
            new_lst.append(elem)
        else:
            for i in range(len(elem)):
                q.enqueue(elem[i])

    return new_lst

lst = [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
new_lst = flatten_list_by_depth(lst)
print(new_lst) #→ [3, 9, 1, 2, 4, 8, 5, 6, 0, 7]
