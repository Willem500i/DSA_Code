def is_palindrome(str, low, high):
    if str[low] != str[high]:
        return False
    elif low == high:
        return True
    else:
        return is_palindrome(str, low+1, high-1)

            
print(is_palindrome("racecar", 0, 6))
print(is_palindrome("racecar", 1, 5))
print(is_palindrome("race car", 0, 6))
print(is_palindrome("racecar", 1, 3))