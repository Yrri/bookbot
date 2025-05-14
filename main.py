from stats import (
    word_count, 
    character_count, 
    create_report
)
import sys

def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents

def print_report(book_path, num_words, report):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in report:
        print(i)
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    num_words = word_count(get_book_text(book))
    num_char = character_count(get_book_text(book))
    report = create_report(num_char)
    print_report(book, num_words, report)

main()