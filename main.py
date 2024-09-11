frankenstein = "books/frankenstein.txt"

def main(path_to_book): # extract the text as string
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def word_counter(text): # Count the words
    words = text.split()
    print(len(words))
    return words

def character_counter(word_list): # count of all the symbols in the text    
    char_count = {}
    one_lowercase_string = "".join(word_list).lower()
    for letter in one_lowercase_string:
        if letter in char_count and letter.isalpha():
            char_count[letter] += 1
        elif letter.isalpha():
            char_count[letter] = 1
    print(char_count)
    return char_count


text = main(frankenstein)
list_of_words = word_counter(text)
character_counter(list_of_words)
