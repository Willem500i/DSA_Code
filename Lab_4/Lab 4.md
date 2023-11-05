# 1
```Python
def is_palindrome(s): # runs in theta(n)
	for i in range(len(s)//2): # runs in theta(n)
		if (s[i] != s[len(s) - 1 - i]): # runs in theta(1)
			return False
	return True
```
# 2
``` Python
def is_vowel(l): # runs in theta(1)
	vowels = ['a','e','i','o','u'] # runs in theta(1)
	for i in range(len(vowels)): # runs in 5 = theta(1)
		if vowels[i] == l:
			return True
	return False
	
def reverse_vowels(input_str):
	list_str = list(input_str) # runs in theta(n)
	left = 0 # runs in theta(1)
	right = len(list_str) - 1# runs in theta(1)
	while left <= right: # runs in theta(n)
		print("looping")
		if not (is_vowel(list_str[left])): #theta(1)
			left += 1
		if not (is_vowel(list_str[right])): #theta(1)
			right -= 1 
		if (is_vowel(list_str[left])) and is_vowel(list_str[right]): #theta(1)
			list_str[left], list_str[right] = list_str[right], list_str[left]
			left += 1
			right -= 1

	return "".join(list_str) # runs in theta(n)
```
# 3
``` Python
def sub_array(nums, k): #theta(n)
	window = len(nums) // k # theta(1)
	local_sum =  sum(nums[:window]) # theta(n)
	max_sum = local_sum # theta(1)
	for i in range(window,len(nums)): # theta(n)
		local_sum = local_sum - nums[i - window] + nums[i] #theta(1)
		if local_sum > max_sum: #theta(1)
			max_sum = local_sum #theta(1)
	return max_sum #theta(1)
print(sub_array([1,12,-5,-6,50,3],2))
```
# 4b
```Python
def find_missing(lst): #theta(log(n))
	left = 0 #theta(1)
	right = len(lst) #theta(1)
	mid = (left + right) // 2 #theta(1)
	if (lst[len(lst) - 1] != len(lst)): #theta(1)
	    return len(lst)
	while left <= right and mid < len(lst): #theta(log(n))
		if (lst[mid] == (mid)):#theta(1)
			left = mid + 1
		else:#theta(1)
			right = mid - 1
		mid = (left + right) // 2#theta(1)
	return mid + 1
	
print(find_missing([0,1,2,4,5,6]))
```
# 4c
```Python
def find_missing_unsorted(lst): #theta(n)
	tot = sum(lst) # theta(n)
	expected_tot = sum([i for i in range(len(lst)+1)]) #theta(n)
	return expected_tot - tot
print(find_missing_unsorted([8, 6, 0, 4, 3, 5, 1, 2]))
```