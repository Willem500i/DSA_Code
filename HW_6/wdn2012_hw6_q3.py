from DoublyLinkedList import *

class CompactString:
    def __init__(self, orig_str):
        ''' Initializes a CompactString object representing the string given in orig_str'''
        self.data = DoublyLinkedList()
        if len(orig_str) == 0:
            self.data.add_last(('',0))
            return
        count = 0
        curr = orig_str[0]
        for i in range(len(orig_str)):
            if orig_str[i] == curr:
                count += 1
            else:
                self.data.add_last((curr,count))
                curr = orig_str[i]
                count = 1
        self.data.add_last((curr,count))

    def __add__(self, other):
        ''' Creates and returns a CompactString object that represent the concatenation of self and other,
        also of type CompactString'''
        out = DoublyLinkedList()
        curr = self.data.header.next
        while curr.data:
            out.add_last(curr.data)
            curr = curr.next

        curr = other.data.header.next

        if out.trailer.prev.data[0] == curr.data[0]: # combine like terms if applicable
            a = out.delete_last()
            out.add_last((a[0],a[1] + curr.data[1]))
            curr = curr.next

        while curr.data:
            out.add_last(curr.data)
            curr = curr.next

        a = CompactString('')
        a.data = out
        return a
    
    def __lt__(self, other): # <
        ''' returns True if self is lexicographically less than other, also of type CompactString'''
        left = self.data.header.next
        right = other.data.header.next

        while (left.data):
            if right.data is None: # right is shorter should return false
                return False
            if left.data[0] == right.data[0]: # if same char
                # if its the end, right should be longer
                # if its the middle, right should be shorter
                if left.data[1] != right.data[1]:
                    if left.next.data and right.next.data:
                        return left.data[1] > right.data[1]
                    else:
                        return left.data[1] < right.data[1]
            else: # if different char, compare alphabetical order
                return left.data[0] < right.data[0]
            
            left = left.next
            right = right.next

        return right.data is not None # longer right should return true

    def __le__(self, other): # <=
        ''' returns True if”f self is lexicographically less than or equal to other, also of type CompactString'''
        left = self.data.header.next
        right = other.data.header.next
        equals = len(self.data) == len(other.data)

        while left.data and right.data:
            if left.data != right.data:
                equals = False
            left = left.next
            right = right.next

        return (equals) or (self < other) 
    
    def __gt__(self, other): # self > other
        ''' returns True if”f self is lexicographically greater than other, also of type CompactString'''
        return other < self
    
    def __ge__(self, other): # self >= other
        ''' returns True if”f self is lexicographically greater than or equal to other, also of type CompactString'''
        return other <= self
    
    def __repr__(self):
        ''' Creates and returns the string representation (of type str) of self'''
        curr = self.data.header.next
        ret = ''
        while curr.data:
            ret += (curr.data[0] * curr.data[1])
            curr = curr.next
        return ret

'''
def test_string_comparisons(string_pairs):
    for pair in string_pairs:
        a, b = pair
        regular_comparison = a < b
        compact_a = CompactString(a)
        compact_b = CompactString(b)
        compact_comparison = compact_a < compact_b

        # print(a+b)

        if compact_comparison is not regular_comparison:
            print(f"Regular Comparison: {a} < {b}: {regular_comparison}")
            print(f"CompactString Comparison: {compact_a} < {compact_b}: {compact_comparison}")
            print()

def test_string_comparisons2(string_pairs):
    for pair in string_pairs:
        a, b = pair
        regular_comparison = a > b
        compact_a = CompactString(a)
        compact_b = CompactString(b)
        compact_comparison = compact_a > compact_b

        if compact_comparison is not regular_comparison:
            print(f"Regular Comparison: {a} > {b}: {regular_comparison}")
            print(f"CompactString Comparison: {compact_a} > {compact_b}: {compact_comparison}")
            print()

def test_string_comparisons3(string_pairs):
    for pair in string_pairs:
        a, b = pair
        regular_comparison = a >= b
        compact_a = CompactString(a)
        compact_b = CompactString(b)
        compact_comparison = compact_a >= compact_b

        if compact_comparison is not regular_comparison:
            print(f"Regular Comparison: {a} >= {b}: {regular_comparison}")
            print(f"CompactString Comparison: {compact_a} >= {compact_b}: {compact_comparison}")
            print()

def test_string_comparisons4(string_pairs):
    for pair in string_pairs:
        a, b = pair
        regular_comparison = a <= b
        compact_a = CompactString(a)
        compact_b = CompactString(b)
        compact_comparison = compact_a <= compact_b

        if compact_comparison is not regular_comparison:
            print(f"Regular Comparison: {a} <= {b}: {regular_comparison}")
            print(f"CompactString Comparison: {compact_a} <= {compact_b}: {compact_comparison}")
            print()

string_pairs = [
    ('aaaaabbbaaac', 'aaaaaaacccaaaa'),
    ('', ''),
    ('a', 'a'),
    ('apple', 'banana'),
    ('hello', 'world'),
    ('python', 'java'),
    ('cat', 'dog'),
    ('123', '456'),
    ('abc', 'abcd'),
    ('ab', 'abc'),
    ('abcaa', 'abcaaa'),
    ('xyz', 'xyz'),
    ('programming', 'program'),
    ('openai', 'gpt'),
    ('test', 'testing'),
    ('string', 'str'),
    ('example', 'examples'),
    ('moon', 'sun'),
    ('good', 'bad'),
    ('alpha', 'beta'),
    ('first', 'second'),
    ('apple', 'apples'),
    ('app', 'apple'),
    ('happy', 'sad'),
    ('coffee', 'tea'),
    ('mountain', 'valley'),
    ('ocean', 'river'),
    ('sky', 'earth'),
    ('book', 'novel'),
    ('green', 'blue'),
    ('music', 'dance'),
    ('flower', 'tree'),
    ('bicycle', 'car'),
    ('smile', 'frown'),
    ('summer', 'winter'),
    ('travel', 'stay'),
    ('science', 'art'),
    ('cloud', 'rain'),
    ('silent', 'loud'),
    ('fast', 'slow'),
    ('bright', 'dark'),
    ('up', 'down'),
    ('laugh', 'cry'),
    ('hot', 'cold'),
    ('fire', 'ice'),
    ('133', '313'),
]


s1 = CompactString('aaaaabbbaaac')
s2 = CompactString('aaaaaaacccaaaa')
print(s1 + s2)   # aaaaabbbaaacaaaaaaacccaaaa
print(s2 + s1)   # aaaaaaacccaaaaaaaaabbbaaac 
print(s1 < s2)   # False
print(s2 < s1)   # True
print(s1 <= s2)  # False
print(s2 <= s1)  # True
print(s1 > s2)   # True
print(s2 > s1)   # False
print(s1 >= s2)  # True
print(s2 >= s1)  # False

test_string_comparisons(string_pairs)
test_string_comparisons2(string_pairs)
test_string_comparisons3(string_pairs)
test_string_comparisons4(string_pairs)
'''