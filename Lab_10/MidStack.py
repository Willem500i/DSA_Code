from DoublyLinkedList import *

class MidStack:
    '''
    The middle is defined as the (n + 1)//2 th element, 
    where n is the number of elements in the stack.
    '''
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = self.data.add_first(None)
        self.elems_left = 0
        self.elems_right = 0
    def __len__(self):
        ''' Returns the number of elements in the stack. '''
        return len(self.data)
    def is_empty(self):
        ''' Returns true if stack is empty and false otherwise. '''
        return len(self) <= 1
    def push(self, e):
        ''' Adds an element, e, to the top of the stack. '''
        a = self.data.add_first(e)
        self.elems_left += 1
        if self.elems_left > self.elems_right + 1:
            self.elems_right += 1
            self.elems_left -= 1
            before = self.data.delete_node(self.mid.prev)
            self.data.add_after(self.mid,before)
        return a
    def top(self):
        ''' Returns the element at the top of the stack.
        An exception is raised if the stack is empty. '''
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.header.next.data
    def pop(self):
        ''' Removes and returns the element at the top of the stack.
        An exception is raised if the stack is empty. '''
        if self.is_empty():
            raise Exception("Stack is empty")
        
        a = self.data.delete_first()
        self.elems_left -= 1
        if self.elems_left < self.elems_right:
            self.elems_right -= 1
            self.elems_left += 1
            next = self.data.delete_node(self.mid.next)
            self.data.add_before(self.mid,next)
        return a
    def mid_push(self, e):
        ''' Adds an element, e, to the middle of the stack.
        An exception is raised if the stack is empty. '''
        if self.is_empty():
            raise Exception("Stack is empty")
        a = self.data.add_before(self.mid,e)
        self.elems_left += 1
        if self.elems_left > self.elems_right + 1:
            self.elems_right += 1
            self.elems_left -= 1
            before = self.data.delete_node(self.mid.prev)
            self.data.add_after(self.mid,before)
        return a
    
a = MidStack()
a.push(1) # [1,None]
a.push(2) # [2,None,1]
a.mid_push(3) # [2,3,None,1]
a.push(4) # [4,2,None,3,1]
a.push(5) # [5,4,2,None,3,1]
a.mid_push(10) # [5,4,2,None,10,3,1]

print(a.pop()) # 5 [4,10,2,None,3,1] [4,10,2,None,3,1]
print(a.pop()) # 4 [10,2,3,None,1] [10,2,None,3,1]
print(a.pop()) # 10 [12,3,1,None] [2,3,None,1]
print(a.pop())
print(a.pop())
print(a.pop())

# a = DoublyLinkedList()
# a.add_first(100)
# a.add_first(200)
# a.add_first(300)
# print(a.header.next.next.next.data)
# print(a.header.next.next.prev.data)