def product_evens(n):
    if n == 0:
        return 1
    else:
        return n * product_evens(n-2)
    
print(product_evens(8))