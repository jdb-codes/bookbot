
def get_book_text(book):
    with open(book) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()
