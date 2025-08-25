
def get_word_count(file_path):
    with open(file_path) as file:
        words = file.read()

    length = len(words.split())
    return (f"Found {length} total words")

def get_char_count(file_path):
    with open(file_path) as file:
        chars = file.read().lower()

    words = {}
    for char in chars:
        if char in words:
            words[char] += 1
        else:
            words[char] = 1
    return words

def sort_on(items):
    return items["num"]

def get_line_count(file_path):

    list_of_dictionaries = []
    for char, count in get_char_count(file_path).items():
        list_of_dictionaries.append({"char": char,"num": count})

    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries


    
 