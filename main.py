def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_book_word_count(text)
    letter_count = get_book_character_count(book_path)


   

def get_book_text(path):
     with open(path) as f:
        return f.read()

def get_book_word_count(text):
    words = text.split()
    return len(words)

def get_book_character_count(path):
    text = get_book_text(path)
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
    