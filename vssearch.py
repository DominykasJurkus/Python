def search4vowels():
    """Display any vowels found in a provided word."""
    vowels = set("aeiou")
    word = input("Provide a word/sentence: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels()