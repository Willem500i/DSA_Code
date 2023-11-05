def sum_of_squares(n):
    return sum([i**2 for i in range(0,n)])

def sum_of_odd_squares(n):
    return sum([i**2 for i in range(0,n) if i % 2 != 0])