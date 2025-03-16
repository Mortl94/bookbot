
from stats import count_words, count_chars, sort_desc
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 1:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    char_dict = count_chars(text)
    char_dict_sorted= sort_desc(char_dict)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for item in char_dict_sorted:
        print(f'{item}: {char_dict[item]}')
    print('============= END ===============')
if __name__ == '__main__':
    main() 