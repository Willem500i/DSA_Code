def find_duplicates(lst): # total runtime theta(n)
    possible_dupes = [0] * len(lst) # theta(n)
    dupes = []
    for i in range(len(lst)): # theta(n)
        possible_dupes[lst[i]] += 1
    for i in range(len(lst)):# theta(n)
        if possible_dupes[i] > 1:
            dupes = dupes + [i]
    return dupes # theta(n)
        
# lst = [1,2,2,2,2,3,4,5,6,7,6,7,9,9]
# print(find_duplicates(lst))