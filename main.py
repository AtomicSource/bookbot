
def get_book_text(file_path):
    book_contents = ""
    with open(file_path) as f:
        # read file
        book_contents = f.read()
    return book_contents 

def main():
    file_path = "books/frankenstein.txt"
    book_contents = get_book_text(file_path)
    print(book_contents)

main()