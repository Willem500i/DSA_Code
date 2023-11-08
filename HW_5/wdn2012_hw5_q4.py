from ArrayStack import *

class Queue():
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()

    def __len__(self):
        return len(self.stack1)+len(self.stack2)
    def is_empty(self):
        return len(self.stack1)+len(self.stack2) == 0
    def enqueue(self,e): # (2+4+6+2n)/n = (n^2+n)/n = theta(n)
        while self.stack1:
            self.stack2.push(self.stack1.pop())
        self.stack2.push(e)
        while self.stack2:
            self.stack1.push(self.stack2.pop())
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.stack1.pop()
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.stack1.top()

# a =Queue()
# a.enqueue(1)
# a.enqueue(2)
# a.enqueue(3)
# a.dequeue()
# print(a.first())