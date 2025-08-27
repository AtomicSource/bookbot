
def get_book_text(file_path:str):
    book_contents = ""
    with open(file_path) as f:
        # read file
        book_contents = f.read()
    return book_contents 

def get_word_number(contents:str):
    words = contents.split()
    number_of_words = len(words)
    return number_of_words

def main():
    file_path = "books/frankenstein.txt"
    book_contents = get_book_text(file_path)
    number_of_words = get_word_number(book_contents)
    print(number_of_words, "words found in the document")

main()