from stats import get_word_count
from stats import get_character_count

def get_book_text(file_path:str):
    book_contents = ""
    # TODO handle exception?
    with open(file_path) as f:
        # read file
        book_contents = f.read()
    return book_contents 

def main():
    file_path = "books/frankenstein.txt"
    book_contents = get_book_text(file_path)
    number_of_words = get_word_count(book_contents)
    print(number_of_words, "words found in the document")
    character_dict = get_character_count(book_contents)
    print(character_dict)

main()