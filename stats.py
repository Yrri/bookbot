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

def create_report(dict, words, book):
    sorted_list = []
    sorted_list.append("============ BOOKBOT ============")
    sorted_list.append(f"Analyzing book found at {book}...")
    sorted_list.append("----------- Word Count ----------")
    sorted_list.append(f"Found {words} total words")
    sorted_list.append("--------- Character Count -------")
    
    for i in sorted(dict, key=dict.get, reverse=True):
        sorted_list.append(f"{i}: {dict[i]}")
    sorted_list.append("============= END ===============")
    return sorted_list
