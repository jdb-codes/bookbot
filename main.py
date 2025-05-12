from stats import get_num_words

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()
