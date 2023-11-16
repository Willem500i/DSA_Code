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

        while (end1.data or end2.data):
            p1, p2 = 0, 0
            if end1.data:
                p1 = int(end1.data)
            if end2.data:
                p2 = int(end2.data)

            all = p1 + p2 + carryover # add elems, with any previous carryover
            tot = all % 10
            carryover = all // 10

            ret = str(tot) + ret
            if end1.data:
                end1 = end1.prev
            if end2.data:
                end2 = end2.prev

        if carryover > 0:
            ret = '1' + ret

        return Integer(ret)
    
    def __mul__(self, other):
        ''' Creates and returns an Integer object that 
        represent the multiplication of self and other, also of type Integer'''

        out = Integer('0')

        end1 = self.data.trailer.prev
        tens = 0
        carryover = 0

        while end1.data:
            ret = '0' * tens # adjust for bigger values each iteration
            end2 = other.data.trailer.prev
            while end2.data:
                tot = int(end1.data) * int(end2.data) + carryover
                carryover = 0

                carryover = tot // 10
                tot %= 10

                print(tot)

                ret = str(tot) + ret
                end2 = end2.prev

            if carryover > 0:
                ret = str(carryover) + ret

            if ret != '': # dont add blank int
                out += Integer(ret)

            end1 = end1.prev
            tens += 1
            carryover = 0

            print(out)

        return out

    def __repr__(self):
        ''' Creates and returns the string representation of self'''
        ret = ''
        curr = self.data.header.next
        while curr.data:
            ret += curr.data
            curr = curr.next

        return ret
    
# '''
# testing
nums = (12345,6789)
n1 = Integer(str(nums[0]))
n2 = Integer(str(nums[1]))
n3 = n1 * n2
print("Multiplication:")
print(f"Expected: {nums[0]} * {nums[1]} = {nums[0]*nums[1]}")
print(f"Realityy: {n1} * {n2} = {n3}\n")
n4 = n1 + n2
print("Addition:")
print(f"Expected: {nums[0]} + {nums[1]} = {nums[0]+nums[1]}")
print(f"Realityy: {n1} + {n2} = {n4}")
# '''