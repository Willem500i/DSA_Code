from ArrayStack import *
operators = "+-*/"
def eval_postfix(lst):
    if len(lst) == 1:
        return lst[0]
    a = ArrayStack()
    for b in lst:
        if str(b).isdigit():
            a.push(int(b))
        else:
            second = a.pop()
            first = a.pop()
            if b == "+":
                a.push(first + second)
            elif b == "-":
                a.push(first - second)
            elif b == "*":
                a.push(first * second)
            elif b == "/":
                a.push(first / second)
    if a:
        return (a.pop())
    return None
# print(eval_postfix(['5','2','*']))
# print(eval_postfix([1]))
# print(eval_postfix([]))

def postfix_calculator():
    str = input("-->")
    while str != "done()":
        name = None
        all = str.split( )
        if '=' in str:
            name = all[0]
            lst = all[2:len(all)]
        else:
            lst = all
        for i in range(len(lst)): # replace globals
            if not lst[i].isdigit() and lst[i] not in operators and globals()[lst[i]]:
                lst[i] = globals()[lst[i]]
        a = eval_postfix(lst)
        if name:
            globals()[name] = a
            print(name)
        else:
            print(a)
        str = input("-->")
        
postfix_calculator()