from ChainingHashTableMap import ChainingHashTableMap

def most_frequent(lst):
    hashmap = ChainingHashTableMap()
    max = (1, lst[0])
    for item in lst:
        try:
            curr = hashmap[item]
            if curr > max[0]:
                max = (curr, item)
            hashmap[item] = curr + 1
        except:
            hashmap[item] = 1
    return max[1]

def first_unique(lst):
    hashmap = ChainingHashTableMap()
    for item in lst:
        try:
            if hashmap[item] == False:
                hashmap[item] = True
        except:
            hashmap[item] = False
    for item in lst:
        if hashmap[item] == False:
            return item

# The complexity shouldn't change with chars instead, because they will just be mapped to ints

def two_sum(lst, target):
    hashmap = ChainingHashTableMap()
    ret = (None, None)
    for i in range(len(lst)):
        hashmap[lst[i]] = i
        if hashmap[target - lst[i]]:
            return (target - lst[i], i)