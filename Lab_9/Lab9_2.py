import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDeque:
    def __init__(self):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.front_ind = None
        self.back_ind = None
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)
    
    def is_full(self):
        return self.n == self.capacity
    
    def resize(self, new_cap):
        new_arr = make_array(new_cap)
        ind = 0
        if (self.front_ind < self.back_ind):
            for i in range(self.front_ind,self.back_ind + 1):
                new_arr[ind] = self.data_arr[i]
                ind += 1
        else:
            for i in range(self.front_ind,self.capacity):
                new_arr[ind] = self.data_arr[i]
                ind += 1
            for i in range(0,self.back_ind):
                new_arr[ind] = self.data_arr[i]
                ind += 1
        self.data_arr = new_arr
        self.capacity = new_cap
    
    def enqueue_first(self, item):
        if(self.is_full()):
            self.resize(self.capacity * 2)
        elif(self.is_empty()):
            self.data_arr[0] = item
            self.front_ind = 0
            self.back_ind = 0
            self.n += 1
        # else:
        #     self.front_ind = (self.front_ind + 1) % self.capacity
        #     self.data_arr[self.front_ind] = item
        #     self.n += 1
        elif (self.front_ind == 0): # array is full from the front
            self.front_ind = self.capacity - 1
            self.data_arr[self.front_ind] = item
            self.n += 1
        else:
            self.front_ind -= 1
            self.data_arr[self.front_ind] = item
            self.n += 1

    def enqueue_last(self, item):
        if(self.is_full()):
            self.resize(self.capacity * 2)
        elif(self.is_empty()):
            self.data_arr[0] = item
            self.front_ind = 0
            self.back_ind = 0
            self.n += 1
        else:
            self.back_ind += 1
            self.data_arr[self.back_ind] = item
            self.n += 1

    def dequeue_first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        return value
    
    def dequeue_last(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.back_ind]
        self.data_arr[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % self.capacity
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        return value

    def first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]
    
    def last(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.back_ind]
    

a = ArrayDeque()
a.enqueue_first(1)
a.enqueue_last(2)
a.enqueue_last(3)
a.enqueue_first(0)
a.enqueue_last(4)
a.enqueue_first(-1)
print(a.dequeue_last())
print(a.dequeue_first())
print(a.dequeue_last())
print(a.dequeue_last())

