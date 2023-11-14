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

            tot = p1 + p2 + carryover # add elems, with any previous carryover
            if tot >= 10: # if sum greater than ten, take 10 and add one to prev carryover
                tot -= 10
                carryover = 1
            else:
                carryover = 0
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

        # get last elem of both
        end1 = self.data.trailer.prev
        tens = 0
        carryover = 0
        '''
        560 *
        230
        = 128800

        0 * 0 = 0
        0 * 3 = 0
        0 * 2 = 0
        out = 0 + 0 = 0

        6 * 0 = 0
        6 * 3 = 8 + carryover
        6 * 2 + 1 = 3 + carryover
        1380 + 0 = 13800

        5 * 0 = 0
        5 * 3 = 5 + carryover
        5 * 2 + 1 = 1 + carryover
        1150 + 00 = 115000 

        13800 + 115000 = 128800
        '''


        while end1.data:
            ret = '0' * tens # adjust for bigger values each iteration
            end2 = other.data.trailer.prev
            while end2.data:
                tot = int(end1.data) * int(end2.data) + carryover
                carryover = 0

                if tot >= 10:
                    carryover = tot // 10
                    tot %= 10

                ret = str(tot) + ret
                end2 = end2.prev


            if carryover > 0:
                ret = str(carryover) + ret

            if ret != '': # dont add blank int
                out += Integer(ret)

            end1 = end1.prev
            tens += 1
            carryover = 0

        return out

    def __repr__(self):
        ''' Creates and returns the string representation of self'''
        ret = ''
        curr = self.data.header.next
        while curr.data:
            ret = ret + curr.data
            curr = curr.next

        return ret

# testing
'''
nums = (23348389,2493)
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
'''