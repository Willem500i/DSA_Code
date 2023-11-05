from ArrayQueue import *

'''
Implement a Stack using just a Queue as the main underlying data collection.
You may only access the ArrayQueue's methods which include: 
len, is_empty, enqueue, dequeue, and first.
'''

class QueueStack:
    def __init__(self):
        self.data = ArrayQueue()
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    # a optimize push
    def push(self, e):
        ''' Add element e to the top of the stack '''
        self.data.enqueue(e)
    def pop(self):
        ''' Remove and return the top element from the stack.
        If the stack is empty, raise an exception'''
        if self.is_empty():
            raise Exception("Stack is empty")
        new_q = ArrayQueue()
        for i in range(len(self) - 1):
            new_q.enqueue(self.data.dequeue())
        ret = self.data.dequeue()
        self.data = new_q
        return ret
    def top(self):
        ''' Return a reference to the top element of the stack without removing it. 
        If the stack is empty, raise an exception '''
        if self.is_empty():
            raise Exception("Stack is empty")
        new_q = ArrayQueue()
        for i in range(len(self) - 1):
            new_q.enqueue(self.data.dequeue())
        ret = self.data.dequeue()
        new_q.enqueue(ret)
        self.data = new_q
        return ret
        
    # b optimize pop
    def push(self, e):
        ''' Add element e to the top of the stack '''
        new_q = ArrayQueue()
        new_q.enqueue()
        while self.data:
            new_q.enqueue(self.data.dequeue())
        self.data = new_q
    def pop(self):
        ''' Remove and return the top element from the stack.
        If the stack is empty, raise an exception'''
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.dequeue()
    def top(self):
        ''' Return a reference to the top element of the stack without removing it. 
        If the stack is empty, raise an exception '''
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.first()