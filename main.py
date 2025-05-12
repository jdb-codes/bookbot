from stats import get_num_words
from stats import get_letter_count
from stats import get_sorted_dict
import sys

def get_book_text(book):
    with open(book) as f:
        return f.read()

def print_report(book_location, word_count, letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in letter_count:
        print(f"{dict["name"]}: {dict["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_location = sys.argv[1]
    num_words = get_num_words(get_book_text(book_location))
    letter_count = get_letter_count(get_book_text(book_location))
    letter_count_sorted = get_sorted_dict(letter_count)
    print_report(book_location, num_words, letter_count_sorted)

main()
