def factors(num): # theta(sqrt(n))
    '''
    int num
    returns generator with num’s divisors in an ascending order
    '''
    factors = [] # theta(1)
    for i in range(1,int(num**0.5)): # theta(sqrt(n))
        if (num % i == 0):# theta(1)
            yield i
    for i in range(int(num**0.5),0, -1): # theta(sqrt(n))
        if (num % i == 0): # theta(1)
            yield num // i

lst = [curr_factor for curr_factor in factors(3)]
print(lst)
lst = [curr_factor for curr_factor in factors(16)]
print(lst)