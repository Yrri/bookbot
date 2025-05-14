from stats import word_count, character_count, create_report

def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents

def main():
    num_words = word_count(get_book_text("books/frankenstein.txt"))
    num_char = character_count(get_book_text("books/frankenstein.txt"))
    report = create_report(num_char, num_words, "books/frankenstein.txt")
    for i in report:
        print(i)
main()