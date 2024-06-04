def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_book_word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} were found in the document")
    letter_count = get_book_character_count(text)
    sorted = sort_letter_dict(letter_count)
    for letters in sorted:
        print(f"The letter '{letters["char"]}' was found {letters["num"]} times.")
    print("--- END OF REPORT ---")


   

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

def sort_on(dict):
    return dict["num"]

def sort_letter_dict(letter_dict):
    sorted_letter_dict = []
    for entries in letter_dict:
        if entries.isalpha():
            sorted_letter_dict.append({"char": entries, "num":letter_dict[entries]})
    sorted_letter_dict.sort(reverse=True, key=sort_on)
    return sorted_letter_dict
        



main()
    