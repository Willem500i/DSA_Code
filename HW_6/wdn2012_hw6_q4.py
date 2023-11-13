from DoublyLinkedList import *

def copy_linked_list(lnk_lst):
    '''
    Creates shallow copy of a nested doubly linked list lnk_lst
    '''
    new_lst = DoublyLinkedList()
    curr = lnk_lst.header.next
    for i in range(len(lnk_lst)):
        new_lst.add_last(curr.data)
        curr = curr.next
    return new_lst
'''
lnk_lst1 = DoublyLinkedList()
elem1 = DoublyLinkedList()
elem1.add_last(1)
elem1.add_last(2)
lnk_lst1.add_last(elem1)
elem2 = 3
lnk_lst1.add_last(elem2)

lnk_lst2 = copy_linked_list(lnk_lst1)
e1 = lnk_lst1.header.next
e1_1 = e1.data.header.next
e1_1.data = 10
e2 = lnk_lst2.header.next
e2_1 = e2.data.header.next
print(e2_1.data) # 10
'''

def deep_copy_linked_list(lnk_lst):
    '''
    Creates deep copy of a nested doubly linked list lnk_lst
    '''
    new_lst = DoublyLinkedList()
    curr = lnk_lst.header.next
    for i in range(len(lnk_lst)):
        if type(curr.data) is int:
            new_lst.add_last(curr.data)
        else:
            new_lst.add_last(deep_copy_linked_list(curr.data))

        curr = curr.next
    return new_lst

'''
lnk_lst1 = DoublyLinkedList()
elem1 = DoublyLinkedList()
elem1.add_last(1)
elem1.add_last(2)
lnk_lst1.add_last(elem1)
elem2 = 3
lnk_lst1.add_last(elem2)

lnk_lst2 = deep_copy_linked_list(lnk_lst1)
e1 = lnk_lst1.header.next
e1_1 = e1.data.header.next
e1_1.data = 10
e2 = lnk_lst2.header.next
e2_1 = e2.data.header.next
print(e2_1.data) # 1
'''