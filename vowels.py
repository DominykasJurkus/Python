vowels = ['a', 'i', 'o', 'u', 'e']
word = input("Provide a word/sentence: ")

found = {}

found['a'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
found['e'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, "was found", v, "time(s).")

