
def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents

def word_count(string):
    num_words = len((string.split()))
    return num_words

def main():
    num_words = word_count(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()