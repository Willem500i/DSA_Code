from ArrayStack import *
from ArrayList import *

def stack_sum(s): 
    """
    : s type: ArrayStack 
    : return type: int 
    """
    if len(s) == 1:
        return s.top()
    else:
        val = s.pop()
        sum = stack_sum(s)
        sum += val
        s.push(val)
        return sum

# a = ArrayStack()
# b = [1, -14, 5, 6, -7, 9, 10, -5, -8]
# for i in range(len(b)):
#     a.push(b[i])
# print(stack_sum(a))
# print(a.top())

def eval_prefix(exp_str): 
    """
    : exp type: str
    : return type: int
    """
    a = ArrayStack()
    exp_lst = exp_str.split( )
    i = len(exp_lst) - 1
    while i >= 0:
        if exp_lst[i].isdigit():
            a.push(exp_lst[i])
        else:
            first = int(a.pop())
            second = int(a.pop())
            if exp_lst[i] == "*":
                a.push(first * second)
            elif exp_lst[i] == "/":
                a.push(first / second)
            elif exp_lst[i] == "-":
                a.push(first - second)
            elif exp_lst[i] == "+":
                a.push(first + second)
        i -= 1
    return a.pop()
'''
print(eval_prefix("- * 3 4 10")) # 2
print(eval_prefix("+ * 5 5 / 10 2")) # 30
print(eval_prefix("+ / - 10 2 4 8")) # 10
'''

def flatten_lst(lst):
    s = ArrayStack()
    for i in range(len(lst)): # move lst to stack
        s.push(lst.pop())
    while s:
        a = s.pop()
        if isinstance(a,int):
            lst.append(a)
        else:
            for i in range(len(a)-1,-1,-1):
                s.push(a[i])

    
# lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
# flatten_lst(lst)
# print(lst)

def stack_sort(s): 
    """
    : input_str type: ArrayStack 
    : return type: None
    """
    helper_stack = ArrayStack( )
    for i in range(len(s)):
        min = s.pop() # get smallest val
        while i < len(s): # go through all of s from where is good (0 at start)
            a = s.pop()
            if not helper_stack:
                helper_stack.push(a)
            elif a < min:
                helper_stack.push(min)
                min = a
            else: # a > min
                helper_stack.push(a)
        s.push(min)
        while helper_stack:
            s.push(helper_stack.pop())

a = ArrayStack()
b = [9,4,6,2,3,7]
for i in range(len(b)):
    a.push(b[i])
stack_sort(a)
while a:
    print(a.pop())

