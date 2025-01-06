def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    text_cut = text[:100]
    letter_dict = get_num_characters(text)
    print(letter_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_characters(text):
    letters = {} 
    for letter in text:
        lowered = letter.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters
        



main()
