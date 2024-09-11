frankenstein = "books/frankenstein.txt"

def main(path_to_book): # extract the text as string
    with open(path_to_book) as f:
        file_contents = f.read()
    text = file_contents
    list_of_words,word_count = word_counter(text)
    char_dict = character_counter(list_of_words)
    list_of_dict = [{"letter" : l, "count": n} for l,n in char_dict.items()]
    list_of_dict.sort(reverse=True, key=lambda x : x["count"])

    print(f"--- Begin report of books/frankenstein.txt ---\n{word_count} words found in the document\n")
    for d in list_of_dict:
        print(f"The '{d['letter']}' character was found {d['count']} times")
    print("--- End report ---")

def word_counter(text): # Count the words
    words = text.split()
    word_count = len(words)
    return words,word_count

def character_counter(word_list): # count of all the symbols in the text    
    char_count = {}
    one_lowercase_string = "".join(word_list).lower()
    for letter in one_lowercase_string:
        if letter in char_count and letter.isalpha():
            char_count[letter] += 1
        elif letter.isalpha():
            char_count[letter] = 1
    return char_count
    
main(frankenstein)

