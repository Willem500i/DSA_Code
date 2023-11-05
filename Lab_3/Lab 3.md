# Vitamins
## 1
Big O - $O(g(n))$ - f(n) is upper bounded by g(n) 
	$f(n) <= c g(n)$ for all $n>= n_0$
Big $\Omega$ - $\Omega(g(n))$ - f(n) is lower bounded by g(n)
	$f(n) >= c g(n)$ for all $n>= n_0$
Big $\Theta$ - $\Theta(g(n))$ - same $\Omega$ and $O$
	$c_2 g(n) <= f(n) <= c_1 g(n)$ for all $n >= n_0$
### a
$n^2 + 5n -2 = O(n^2)$
Let $f(n) = n^2 + 5n -2$
$f(n) <= c g(n)$ for all $n>= n_0$
1. $n^2+5n-2 \leq$
2. $n^2+5n^2-2 \leq$
3. $6n^2$
Conclusion: $6n^2 \ge n^2+5n-2$
$f(n)$ is $O(n^2)$ because we can set $c=6$ and $n_0=1$
### b
$\frac{n^2-1}{n+1} = O(n)$
$f(n)=\frac{n^2-1}{n+1}$
$\frac{n^2-1}{n+1} = \frac{(n+1)(n-1)}{n+1} = n-1$
$n-1 \leq n+n \leq 2n$
$f(n)$ is $O(n)$ because we can set $c=2$ and $n_0=1$
### c
$f(n)=\sqrt{5n^2-3n+2} = \Theta(n)$ 
$\sqrt{5n^2-3n+2} \ge \sqrt{5n^2-3n+2n} \ge \sqrt{5n^2-n^2} \ge \sqrt{4n^2} \ge 2n$
$\sqrt{5n^2-3n+2} \leq \sqrt{20n^2-12n+8} \leq\sqrt{20n^2-12n^2}\leq\sqrt{8n^2}\leq\sqrt{8}n$
$f(n)$ is $\Theta(n)$ because we can set $c_1=2$, $c_2=\sqrt{8}$ and $n_0=1$

## 2
### a
True, because $8n^2\sqrt{n} = 8n^{2.5}$, and  $8n^{2.5} \leq n^3$ for $c = 8$ and $n_0 = 64$
### b
False, because $8n^2\sqrt{n} = 8n^{2.5}$ and $c*n^3 >= 8n^{2.5}$ because there will never be a const that makes this false 
## 3
$f_6(n)=1 =$
$f_{10}(n)=700 \leq$
$f_5(n)=\sqrt{log(n)} \leq$
$f_3(n)=\sqrt{n}=$
$f_{12}(n)=\sqrt{9n}\leq$
$f_4(n)=log(\sqrt{n}) =$
$f_{11}(n)=log(n) \leq$
$f_9(n)=\frac{n}{log(n)} \leq$
$f_{16}(n)=\frac{n}{3}=$
$f_1(n)=n =$
$f_2(n)=500n \leq$
$f_8(n)=n\cdot log(n)\leq$
$f_{17}(n)=\sqrt{n^3} \leq$
$f_{14}(n)=n^2 \leq$
$f_{15}(n)=n^3 \leq$
$f_{13}(n)=2^n \leq$
$f_7(n)=3^n \leq$
$f_{18}(n)=n!$
## 4
$1+1$
2
$2+1$
3
$3+2$
5
$4+2$
6
$5+3$
8
$6+3$
9
$7+4$
11
12
14
$10+5$
15
$2,3,5,6,8,9,11,12,14,15$
# Coding
## 1
### a
``` Python
def reverse_list(lst):
	for i in range(len(lst)//2):
		tmp = lst[i]
		tmp2 = lst[len(lst)-1-i]
		lst[len(lst)-1-i] = tmp
		lst[i] = tmp2

lst = [1,2,3,4,5,6,7]
reverse_list(lst)
print(lst)
```
### b
```Python
def reverse_list(lst, low = None, high = None):
	if not low:
		low = 0
	if not high:
		high = len(lst) - 1
	while (low < high):
		lst[low], lst[high] = lst[high], lst[low]
		low += 1
		high -=1
		
lst = [1,2,3,4,5,6]
reverse_list(lst,1,3)
print(lst)
```

## 2
```Python
def powers_of_two(n):
	return [2**i for i in range(n)]
print(powers_of_two(6))
```
## 3
```Python
def move_zeros(nums):
	zeros = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[i], nums[zeros] = nums[zeros], nums[i]
			zeros += 1
lst = [1,0,9,0,13,0,0,34]
move_zeros(lst)
print(lst)
```
## 4
``` Python
def reverse_list(lst, low = 0, high = len(lst)-1):
	while (low < high):
		lst[low], lst[high] = lst[high], lst[low]
		low += 1
		high -=1
def shift(lst, k):
	reverse_list(lst)
	reverse_list(lst,0,k-1)
	reverse_list(lst,k,len(lst)-1)
	

lst = [1, 2, 3, 4, 5, 6]
shift(lst, 2) # [5, 6, 1, 2, 3, 4]
print(lst)
```
