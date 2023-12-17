import random
from DoublyLinkedList import DoublyLinkedList

import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ChainingHashTableSet:

    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N

    def __init__(self, N=64):
        self.table = make_array(N)
        for i in range(N):
            self.table[i] = DoublyLinkedList()
        self.n = 0
        self.h = ChainingHashTableSet.MADHashFunction(N)


    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def add(self, key):
        i = self.h(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket.add_last(key)

        new_size = len(curr_bucket)
        if (new_size > old_size):
            self.n += 1
        if (self.n > len(self.table)):
            self.rehash(2 * len(self.table))

    def remove(self, key):
        i = self.h(key)
        curr_bucket = self.table[i]
        curr = curr_bucket.header
        running = True
        while curr is not curr_bucket.trailer and running:
            if curr.data == key:
                curr_bucket.delete_node(curr)
                running = False
            curr = curr.next
        self.n -= 1
        if (self.n < len(self.table) // 4):
            self.rehash(len(self.table) // 2)

    def __contains__(self, key):
        try:
            val = self[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        for curr_bucket in self.table:
            yield from curr_bucket

    def rehash(self, new_size):
        old = [key for key in self]
        self.__init__(new_size)
        for (key) in old:
            self.add(key)


def print_hash_table(hset):
    for item in hset: print(item)