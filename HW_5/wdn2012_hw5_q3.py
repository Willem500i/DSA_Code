from ArrayStack import *
from ArrayDeque import *

class MidStack():
    def __init__(self):
        self.left = ArrayStack()
        self.right = ArrayDeque()
    def __len__(self):
        return len(self.left) + len(self.right)
    def is_empty(self):
        return len(self.left) + len(self.right) == 0
    def push(self,e):
        self.right.enqueue_last(e)
        if len(self.left) < len(self.right):
            self.left.push(self.right.dequeue_first())
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if self.right:
            a = self.right.dequeue_last()
        else:
            a = self.left.pop()
        if len(self.left) > len(self.right)+1:
            self.right.enqueue_first(self.left.pop())
        return a
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.right.last()
    def mid_push(self, e):
        self.left.push(e)
        if len(self.left) > len(self.right)+1:
            self.right.enqueue_first(self.left.pop())
# midS = MidStack() 
# midS.push(2)
# midS.push(4)
# midS.push(6)
# midS.push(8)
# midS.push(10)
# midS.mid_push(12)
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())

