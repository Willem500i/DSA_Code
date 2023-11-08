from ArrayStack import *
from ArrayQueue import *

def permutations(lst):
    stack = ArrayStack() # stores elements still to be used
    queue = ArrayQueue() # stores already created permutations

    for elem in lst:
        stack.push(elem)
    queue.enqueue([stack.pop()])
    while stack:
        var = stack.pop()
        curr = queue.dequeue()
        depth = len(curr)
        while len(curr) == depth:
            for i in range(depth+1):
                new = curr.copy()
                new.insert(i,var)
                queue.enqueue(new)
            curr = queue.dequeue()
        queue.enqueue(curr)
            
    return [queue.dequeue() for i in range(len(queue))]


# print(permutations([1,2,3]))