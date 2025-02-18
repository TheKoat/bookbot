def count_words(text):
    count = len(text.split())
    return count

def count_characters(text):
    count_dict = {}
    for word in text.lower():
        for char in word:
            count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict

def sort_on(dict):
    return dict[1]

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        words_count = count_words(file_contents)
        characters_count_dict = count_characters(file_contents)
        print(f"--- Begin report of {book_path} ---")
        print(f"{words_count} words found in this document\n\n")
        
        characters_count_list = list(characters_count_dict.items())
        characters_count_list.sort(reverse=True, key=sort_on)
        
        for character in characters_count_list:
            if character[0].isalpha():
                print(f"The '{character[0]}' character was found {character[1]} times")
        
        print("--- End Report ---")


main()