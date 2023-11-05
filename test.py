lst1 = [1,2,[3,4]]
lst2 = lst1
lst3 = lst1 + lst2
lst2[0] = 10
lst2[2][0] = 30
print(lst1)
print(lst2)
print(lst3)