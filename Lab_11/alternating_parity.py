from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

def alternating_parity(lst):
    queue = ArrayQueue()
    stack = ArrayStack()
    curr = True
    count = 0
    while count < len(lst):
        elem = lst[count]
        if queue and ((curr is True and queue.first() % 2 == 0) or (curr is False and queue.first() % 2 != 0)):
            stack.push(queue.dequeue())
            curr = not curr
        elif (curr is True and elem % 2 == 0) or (curr is False and elem % 2 != 0):
            stack.push(elem)
            curr = not curr
            count += 1
        else:
            queue.enqueue(elem)
            count += 1
    while queue:
        stack.push(queue.dequeue())
    for i in range(len(lst)-1,-1,-1):
        lst[i] = stack.pop()

# lst = [2,4,6,8,3,5,7,9,10,11,13,15,17,12,14,16,18,6,7,9,8]
lst = [3,6,2,17,13,3,2,20,17,6]
alternating_parity(lst)
print(lst)