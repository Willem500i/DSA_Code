from DoublyLinkedList import *

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()
    def __len__(self):
        ''' Returns the number of elements in the stack. '''
        return len(self.data)
    def is_empty(self):
        ''' Returns true if the stack is empty,false otherwise. '''
        return self.data.is_empty()
    def push(self, e):
        ''' Adds an element, e, to the top of the stack. '''
        self.data.add_last(e)
    def top(self):
        ''' Returns the element at the top of the stack.
        An exception is raised if the stack is empty. '''
        return self.data.trailer.prev.data
    def pop(self):
        ''' Removes and returns the element at the top of the stack.
        An exception is raised if the stack is empty. '''
        return self.data.delete_last()
a = LinkedStack()
a.push(1)
a.push(2)
a.push(3)
print(a.top())
print(a.pop())
print(a.pop())