def word_count(string):
    num_words = len((string.split()))
    return num_words

def character_count(string):
    characters = {}
    for char in string.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def create_report(dict):
    sorted_list = []
    for i in sorted(dict, key=dict.get, reverse=True):
        if not i.isalpha():
            continue
        sorted_list.append(f"{i}: {dict[i]}")
    return sorted_list
