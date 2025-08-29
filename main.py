from stats import get_word_count
from stats import get_character_counts
from stats import sort_character_counts
from stats import CHAR, COUNT

def get_book_text(file_path:str):
    book_contents = ""
    # TODO handle exception?
    with open(file_path) as f:
        # read file
        book_contents = f.read()
    return book_contents 

def main():
    print("============ BOOKBOT ============")
    file_path = "books/frankenstein.txt"
    book_contents = get_book_text(file_path)
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    number_of_words = get_word_count(book_contents)
    print("Found", number_of_words, "total words")
    print("--------- Character Count -------")
    character_count_dict = get_character_counts(book_contents)
    character_count_list = sort_character_counts(character_count_dict)
    # Print out list of character counts, skipping non-alpha
    for cc in character_count_list:
        if cc[CHAR].isalpha():
            print(f"{cc[CHAR]}: {cc[COUNT]}")
    print("============= END ===============") 

main()
