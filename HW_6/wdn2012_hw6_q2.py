from DoublyLinkedList import *

class Integer():
    def __init__(self, num_str):
        ''' Initializes an Integer object representing
        the value given in the string num_str'''
        self.data = DoublyLinkedList()
        new_str = num_str
        if num_str != '0':
            new_str = num_str.lstrip('0')
        for i in new_str:
            self.data.add_last(i)
    def __add__(self, other):
        ''' Creates and returns an Integer object that represent 
        the sum of self and other, also of type Integer'''
        ret = ''

        # get last elem of both
        end1 = self.data.trailer.prev
        end2 = other.data.trailer.prev
        carryover = 0

        while (end1.data and end2.data):
            tot = int(end1.data) + int(end2.data) + carryover # add elems, with any previous carryover
            if tot >= 10: # if sum greater than ten, take 10 and add one to prev carryover
                tot -= 10
                carryover = 1
            else:
                carryover = 0
            ret = str(tot) + ret
            end1 = end1.prev
            end2 = end2.prev
        
        while end1 and end1.data:
            tot = int(end1.data) + carryover
            if tot >= 10:
                tot -= 10
                carryover = 1
            else:
                carryover = 0
            ret = str(tot) + ret
            end1 = end1.prev
        while end2 and end2.data:
            tot = int(end2.data) + carryover
            if tot >= 10:
                tot -= 10
                carryover = 1
            else:
                carryover = 0
            ret = str(tot) + ret
            end2 = end2.prev

        if carryover > 0:
            ret = '1' + ret

        return Integer(ret)
    
    def __mul__(self, other):
        ''' Creates and returns an Integer object that 
        represent the multiplication of self and other, also of type Integer'''
        '''

        123 *
        456

        6 * 123 +
        50 * 123 +
        400 * 123
        '''

        end1 = int(float(repr(self)))
        end2 = other.data.trailer.prev

        tens = 1

        tot = Integer('0')

        while end2.data:
            a = str((tens * int(end2.data)) * end1)
            tot = tot + Integer(a)
            tens *= 10
            end2 = end2.prev
        return tot


    def __repr__(self):
        ''' Creates and returns the string representation of self'''
        ret = ''
        curr = self.data.header.next
        while curr.data:
            ret = ret + curr.data
            curr = curr.next

        return ret


# n1 = Integer('999')
# n2 = Integer('10')
# n3 = n1 * n2
# print(n3)
# print(n1.data)
# print(n2.data)
# print(n3.data)