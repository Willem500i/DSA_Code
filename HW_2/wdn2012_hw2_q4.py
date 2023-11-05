def e_approx(n): # theta(n)
    e = 0
    multiplier = 1
    for i in range(1, n+2): # theta(n)
        e += 1 / multiplier # theta(1)
        multiplier *= i # theta(1)
    return e

# for n in range(15):
#     curr_approx = e_approx(n)
#     approx_str = "{:.15f}".format(curr_approx) 
#     print("n =", n, "Approximation:", approx_str)