1.
```Python
def sum_to(n):
    if n == 1:
	    return 1
	else:
		return n + sum_to(n-1)
```