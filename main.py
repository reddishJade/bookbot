from stats import get_num_words, get_num_chars, sort_dict
import sys


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_chars = get_num_chars(text)
    print("--------- Character Count -------")
    # print(num_chars)
    num_chars_sorted = sort_dict(num_chars)
    # print(num_chars_sorted)
    display_result(num_chars_sorted)
    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path, encoding="utf-8-sig") as f:
        return f.read()


def display_result(chars_dict):
    for chars in chars_dict:
        if chars["char"].isalpha():
            char = chars["char"]
            num = chars["num"]
            print(f"{char}: {num}")


main()
