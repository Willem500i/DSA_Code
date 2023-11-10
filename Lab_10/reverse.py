from DoublyLinkedList import *

def reverse_dll_by_data(dll):
     ''' Reverses the linked list '''

     start = dll.header.next
     end = dll.trailer.prev

     tot = len(dll)

     while tot > 0:
          start.data, end.data = end.data, start.data
          start = start.next
          end = end.prev
          tot -= 2

def reverse_dll_by_node(dll):
    ''' Reverses the linked list '''

    curr = dll.header

    while curr is not None:
        curr.prev, curr.next = curr.next, curr.prev
        curr = curr.prev
    
    dll.header, dll.trailer = dll.trailer, dll.header


a = DoublyLinkedList()
a.add_first(1)
a.add_last(2)
a.add_last(3)
a.add_last(4)
print(a)
reverse_dll_by_data(a)
print(a)
reverse_dll_by_node(a)
print(a)