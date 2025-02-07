def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_count = count_words(text)
    char_count = count_characters(text)
    
    print_report(book_path, word_count, char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def print_report(book_path, word_count, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

main()