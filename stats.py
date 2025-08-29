def get_word_count(contents:str):
    words = contents.split()
    number_of_words = len(words)
    return number_of_words

def get_character_counts(contents:str):
    characters = {}
    for char in contents.lower():
        if char in characters:
            characters[char] = characters[char] + 1
        else: 
            characters[char] = 1
    return characters

# define keys for character dictionaries
COUNT = "count"
CHAR = "character"
# to be used as sorting key
def sort_on_count(dict):
    return dict[COUNT]

### takes dictionary of characters returns
### sorted list of dictionaries
def sort_character_counts(characters_dict):
    character_list = []
    for key in characters_dict:
        char = {CHAR : key, COUNT : characters_dict[key]}
        character_list.append(char)
    character_list.sort(reverse = True, key = sort_on_count)
    return character_list
