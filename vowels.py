vowels = ['a', 'i', 'o', 'u', 'e']
word = "Mississippi is a river"

found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
        
for vowel in found:
    print(vowel)

