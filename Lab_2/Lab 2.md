```Python
class Polynomial:
	def __init__(self, coefficients = [0]):
		coefficients.reverse()
		self.coeff = coefficients

	def __add__(self,other):
		out = []
	# assigns the longer list to poly1. Shallow copy because all values are immutable ints
		poly1 = self.coeff if len(self.coeff) > len(other.coeff) else other.coeff
		poly2 = other.coeff if poly1 == self.coeff else self.coeff
		while len(poly1) > len(poly2):
			poly2 = [0] + poly2 # get them to be the same length
		for i in range(len(poly1)):
			out.append(poly1[i]+poly2[i])
		return Polynomial(out)

	def __call__(self,param):
		length = len(self.coeff)
		sum = 0
		for i in range(length):
			power = length - i
			sum += self.coeff[i]* (param**power)
		return sum
# Return solved polynomial

	def __repr__(self): 
		strings = [f"{str(self.coeff(i))}x^{len(self.coeff)-i}" for i in range(len(self.coeff))]
		return "+".join[strings]

poly1 = Polynomial([3, 7, 0, -9, 2]) # represents 2x4 - 9x3 + 7x + 3
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3]) # represents 3x6 + 5x3 + 2
poly3 = poly1 + poly2  

print(poly1(1)) # return 3 
print(poly2(1)) # return 10 
print(poly3(1)) # return 13

	#__mul__(self, other): # OPTIONAL
		#return ""
# return a NEW polynomial

	#__derive__(self): # OPTIONAL
		#return ""
# modify polynomial to have its derived value
```


```Python
class UnsignedBinaryInteger:
	def __init__(self,bin_num_str):
		self.data = bin_num_str
	def decimal(self):
		rev = (self.data)[::-1]
		sum = 0
		for i in range(len(rev)):
			sum += 2**i * int(rev[i])
		return sum
	def __lt__(self,other):
		return self.decimal() < other.decimal()
	def __gt__(self,other):
		return self.decimal() > other.decimal()
	def __eq__(self,other):
		return self.decimal() == other.decimal()
	def is_twos_power(self):
		count = 0
		for num in self.data:
			if num == "1":
				count += 1
		return count == 1
	def largest_twos_power(self):
		return int((self.data)[0]) * 2**(len(self.data) - 1)
	def __repr__(self):
		return f"0b{self.data}"

a = UnsignedBinaryInteger("1001")
b = UnsignedBinaryInteger("1000")
print(a.is_twos_power())
print(b.is_twos_power())
```