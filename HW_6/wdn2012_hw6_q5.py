from DoublyLinkedList import *

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2): # runs in linear time
    ''' Merges two sorted linked lists '''
    def merge_sublists(start1, start2):
        # are start1 and start2 tails
        s1_is_last = start1.next.data is None 
        s2_is_last = start2.next.data is None

        if s1_is_last and s2_is_last:
            return DoublyLinkedList()
        
        if s1_is_last:
            out = DoublyLinkedList()
            curr = start2
            added = False
            while curr.data:
                if start1.data < curr.data and added is False:
                    out.add_last(start1.data)
                    added = True
                out.add_last(curr.data)
                curr = curr.next
            if not added:
                out.add_last(start1.data)
            return out
        
        if s2_is_last:
            out = DoublyLinkedList()
            curr = start1
            added = False
            while curr.data:
                if start2.data < curr.data and added is False:
                    out.add_last(start2.data)
                    added = True
                out.add_last(curr.data)
                curr = curr.next
            if not added:
                out.add_last(start2.data)
            return out

        if start1.data < start2.data:
            out = merge_sublists(start1.next, start2)
            out.add_first(start1.data)
            return out
        else: # start1.data >= start2.data
            out = merge_sublists(start1, start2.next)
            out.add_first(start2.data)
            return out

    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next)


# list_1 = DoublyLinkedList()
# list_1.add_last(2)
# list_1.add_last(4)
# list_1.add_last(7)
# list_1.add_last(10)
# list_1.add_last(23)


# # for i in range(30):
# #     list_1.add_last(i)

# list_2 = DoublyLinkedList()
# for i in range(10,20):
#     list_2.add_last(i)

# a = merge_linked_lists(list_1,list_2)
# print(a)