### 1. Can Construct
``` Python
def can_construct(word, letters): 
    word_letters = list(word)
    guess_letters = list(letters)
      
    for letter in word_letters:
        if letter in guess_letters:
            guess_letters.remove(letter)
        else:
            return False
        
    return True
    
if __name__ == "__main__":
	print(can_construct("apples", "aples"))
	print(can_construct("apples", "aplespl"))
	print(can_construct("apples", "ffjskanfiusa"))
	print(can_construct("apples", "appless"))
	print(can_construct("hello", "helo"))
```
### 2. Complex Numbers
```Python
class Complex:
    def __init__(self, a, b):
        self.real = a;
        self.imaginary = b
        
    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return Complex(r,i)
        
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return Complex(r,i)
        
    def __mul__(self, other):
        F = self.real * other.real
        O = self.real * other.imaginary
        I = self.imaginary * other.real
        L = self.imaginary * other.imaginary
        
        r = F - I
        i = O + L
        
        return Complex(r,i)
        
    def __repr__(self):
        real_sign = "" if self.real > 0 else "-"
        imaginary_sign = "+" if self.imaginary > 0 else "-"
        return f"{real_sign}{abs(self.real)} {imaginary_sign} {abs(self.imaginary)}i"
        
    def __iadd__(self, other):
        self.real = self.real + other.real
        self.imaginary = self.imaginary + other.imaginary
        return self
        
#constructor, output
cplx1 = Complex(5, 2) 
print(cplx1) #5 + 2i

cplx2 = Complex(3, 3) 
print(cplx2) #3 + 3i

#addition
print(cplx1 + cplx2) #8 + 5i

#subtraction
print(cplx1 - cplx2) #2 - 1i

#multiplication
print(cplx1 * cplx2) #9 + 21i

#original objects remain unchanged 
print(cplx1) #5 + 2i 
print(cplx2) #3 + 3i
```

### 3. Randomizer game
```Python
import random

def create_permutation(n):
    # initialize a list with all the numbers
    list_out = []
    
    def get_new_int(exclude,max):
        int = random.randint(0,max-1)
        while int in exclude:
            int = random.randint(0,max-1)
        return int
    
    for i in range(n):
        my_random_int = get_new_int(list_out,n)
        list_out.append(my_random_int)
    return list_out

def scramble_word(word):
    
    new_indicies = create_permutation(len(word))
    word_array = list(word)
    array_out = []
    
    for i in range(len(word)):
        array_out.append(word_array[new_indicies[i]])
    
    word_out = ""
    
    for letter in array_out:
        word_out += letter
        
    return word_out
    
def word_scramble_game():
    words = ["pokemon","go","to","the","polls"]
    word = words[random.randint(0,len(words) - 1)]
    
    scrambled_word = scramble_word(word)
    scrambled_word_string = ""
    
    for letter in scrambled_word:
        scrambled_word_string += f" {letter}"
    
    print(f"Unscramble the word: {scrambled_word_string}\n")
    guess = input('Try #1: ')
    if guess == word:
        print("Yay, you got it!")
    else:
        print("Wrong!")
        guess = input('Try #2: ')
        if guess == word:
            print("Yay, you got it!")
        else: 
            print("Git gud. Wrong again!")
            guess = input('Try #3: ')
            if guess == word:
                print("Yay, you got it!")
            else:
                print("YOU LOSE LOSER!")

word_scramble_game()
```
### 4. Optional Binary Additon
``` Python
def add_binary(bin_num1, bin_num2):
    first_longest = len(bin_num1) > len(bin_num2)
    
    if first_longest:
        while len(bin_num1) > len(bin_num2):
            bin_num2 = "0" + bin_num2
    else:
        while len(bin_num1) < len(bin_num2):
            bin_num1 = "0" + bin_num1
            
    carryover = 0
    out = ""

    for i in reversed(range(len(bin_num1))):
        sum = int(bin_num1[i]) + int(bin_num2[i]) + carryover
        carryover = 0
        if sum == 0:
            out = "0" + out
        elif sum == 1:
            out = "1" + out
        elif sum == 2:
            out = "0" + out
            carryover = 1
        elif sum == 3:
            out = "1" + out
            carryover = 1
        
    if carryover:
        out = "1" + out
    return out
    
print(f"10001 + 10001 = {add_binary('10001','10001')}")
```