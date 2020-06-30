def search4vowels():
    """Display any vowels found in a provided word."""
    vowels = set("aeiou")
    word = input("Provide a word/sentence: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

def search4letters(phrase:str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase))

search4vowels()
print(search4letters("Hmm what to say"))