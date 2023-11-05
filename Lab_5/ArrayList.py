import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, coll = []):
        self.data_arr = make_array(len(coll)+1)
        self.capacity = 1
        self.n = 0

        if (len(coll) > 0):
            for i in range(len(coll)):
                self.append(coll[i])


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if (not (-1 * (self.n) <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if (not (-1 * (self.n) <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)
    
    def __repr__(self):
        # ret = f"[{','.join(self.data_arr[0:self.n])}]"
        ret = "["
        for i in range(self.n):
            ret += str(self.data_arr[i])
            if i != self.n - 1:
                ret += ", "
        return ret + "]"
    
    def __add__(self, other):
        a = ArrayList()
        for i in range(self.n):
            a.append(self[i])
        for j in range(other.n):
            a.append(other[j])
        return a

    def __iadd__(self,other):
        for i in range(other.n):
            self.append(other[i])
        return self 
    
    def __mul__(self, other):
        a = ArrayList()
        for i in range(other):
            a += self
        return a
    
    def __rmul__(self, other):
        return (self * other)
    
    def remove(self,val):
        for i in range(self.n-1, 0, -1):
            if self[i] == val:
                for j in range(i,self.n-1):
                    self[j] = self[j+1]
                self.n -= 1
                return self
    def removeAll(self, val):
        count = 0
        for i in range(self.n - count):
            if self[i-count] == val:
                self[i-count], self[self.n-1-count] =  self[self.n-1-count],self[i-count]
                count +=1
        self.n -= count
        return self

a = ArrayList()
b = ArrayList()
for i in range(5):
    a.append(i)
    b.append(1+i*2)

c = ArrayList([0,1,3,5,2,1,1])
print(c)
c.removeAll(1)
print(c)