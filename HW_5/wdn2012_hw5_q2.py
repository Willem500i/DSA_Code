from ArrayStack import *

class MaxStack():
    def __init__(self):
        self.data = ArrayStack()
        self.maximum = 0

    def is_empty(self):
        return self.data.is_empty()
    
    def __len__(self):
        return len(self.data)
    
    def push(self, val):
        if val > self.maximum:
            self.data.push((val,self.maximum))
            self.maximum = val
        else:
            self.data.push((val,0))
    
    def top(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.data.top()[0]
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        a = self.data.pop()
        if a[0] == self.maximum:
            self.maximum = a[1]
        return a[0]
    def max(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.maximum
    
# maxS = MaxStack()
# maxS.push(1)
# maxS.push(3)
# maxS.push(6)
# maxS.push(4)
# print(maxS.max())
# print(maxS.pop())
# print(maxS.pop())
# print(maxS.max())
# print(maxS.pop())
# print(maxS.max())

