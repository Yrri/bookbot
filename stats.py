def word_count(string):
    num_words = len((string.split()))
    return num_words

def character_count(string):
    characters = {}
    for char in string.lower():
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] = characters.get(char) + 1
    return characters