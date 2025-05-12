from stats import get_num_words
from stats import get_letter_count

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    letter_count = get_letter_count(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(letter_count)

main()
