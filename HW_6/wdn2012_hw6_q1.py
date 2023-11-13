from DoublyLinkedList import *

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    def enqueue(self,item):
        self.data.add_last(item)
    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return(self.data.delete_first())
    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        a = self.data.delete_first()
        self.data.add_first(a)
        return a
    
# a = Queue()
# a.enqueue(1)
# a.enqueue(2)
# a.enqueue(3)
# print(a.first())
# print(a.dequeue())
# print(a.dequeue())
# print(a.dequeue())