def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_book_word_count(text)
    print(word_count)
    letter_count = get_book_character_count(text)
    print(letter_count)


   

def get_book_text(path):
     with open(path) as f:
        return f.read()

def get_book_word_count(text):
    words = text.split()
    return len(words)

def get_book_character_count(text):
    lowered_text = text.lower()
    words = lowered_text.split()
    letter_dict = {}
    for word in words:
        for letter in word:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict


main()
    