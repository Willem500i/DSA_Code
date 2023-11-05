def shift(lst, k, dir = "left"):
    for i in range(k):
        if dir == "left":
            elem = lst.pop(0)
            lst.append(elem)
        else:
            elem = lst.pop(len(lst)-1)
            lst.insert(0, elem)