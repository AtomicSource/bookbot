def get_word_count(contents:str):
    words = contents.split()
    number_of_words = len(words)
    return number_of_words

def get_character_count(contents:str):
    characters = {}
    for char in contents.lower():
        if char in characters:
            characters[char] = characters[char] + 1
        else: 
            characters[char] = 1
    return characters