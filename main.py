from stats import word_count, character, sorted_char
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    total_words = word_count(text)
    char_counts = character(text)
    sorted_characters = sorted_char(char_counts)
    print("=========== BOOKBOT ===========")
    print(f'Analyzing book found at books/{book_path}')
    print("----------- Word Count ----------")
    print(f'Found {total_words} total words')
    print("--------- Character Count -------")

    for item in sorted_characters:
         print(f'{item['char']}: {item['num']}')
    print("============= END ===============")


main()      







