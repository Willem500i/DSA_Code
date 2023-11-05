# a
def count_lowercase(s, low, high):
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        if s[low].islower():
            return 1 + count_lowercase(s, low + 1, high)
        else:
            return count_lowercase(s, low + 1, high)

# b
def is_number_of_lowercase_even(s, low, high):
    if low == high:
        return not s[low].islower()
    else:
        evens = is_number_of_lowercase_even(s, low + 1, high)
        return (s[low].islower() and not evens) or (not s[low].islower() and evens)