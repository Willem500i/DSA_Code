from ArrayQueue import *

class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.tot = 0
        self.n = 0
    def __len__(self):
        return self.n
    def is_empty(self):
        return self.n == 0
    def enqueue(self, e):
        ''' Add element e to the end of the queue. 
        If e is not an int or float, raise a TypeError '''
        if type(e) is not int or float:
            raise TypeError("Only int or float accepted")
        self.n += 1
        self.tot += e 
        self.data.enqueue(e)
    def dequeue(self):
        ''' Remove and return the first element from the queue. 
        If the queue is empty, raise an exception'''
        if self.is_empty():
            raise Exception("Queue is empty")
        self.n -= 1
        a = self.data.dequeue()
        tot -= a
        return a
    def first(self):
        ''' Return a reference to the first element of the queue without removing it. 
        If the queue is empty, raise an exception '''
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.first()
    def sum(self):
        return self.tot
    def mean(self):
        return self.tot / self.n