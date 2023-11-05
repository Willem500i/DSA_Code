vowels = ['a','e','i','o','u']

def vc_count(word, low, high):
    if low == high:
        if word.lower() in vowels:
            return (1,0)
        else:
            return (0,1)
    else:
        if word[low].lower() in vowels:
            tup = vc_count(word, low + 1, high)
            return (tup[0] + 1, tup[1])
        else:
            tup = vc_count(word, low + 1, high)
            return (tup[0], tup[1]+1)

word = "NYUTandonEngineering"
print(vc_count(word, 0, len(word)-1)) # → (8, 12) 8 vowels, 12 consonants
