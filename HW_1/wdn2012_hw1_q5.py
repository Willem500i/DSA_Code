def fibs(n):
    index = 0
    a = 0
    b = 1
    while (index < n):
        tmp = a + b
        a = b
        b = tmp
        index += 1
        yield a