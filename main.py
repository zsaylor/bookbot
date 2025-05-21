from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_char_count
import sys

def main():
    # file_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    word_count = get_word_count(book)
    char_count = get_char_count(book)
    char_count_list = get_sorted_char_count(char_count)
    print(print_report(file_path, word_count, char_count_list))

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def print_report(file_path, word_count, char_count):
    char_count_str = ""
    for char_dict in char_count:
        char_count_str += f"{char_dict["char"]}: {char_dict["num"]}\n"

    return f"""
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{char_count_str}
============= END ===============
"""

main()

