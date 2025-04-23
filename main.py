import sys
from stats import get_num_words, count_unique_characters, sort_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    unique_count = count_unique_characters(text)
    #print(unique_count)
    list_char_count = sort_char_count(unique_count)
    for e in list_char_count:
        if e[0].isalpha():
            print(f"{e[0]}: {e[1]}")
    print("============= END ===============")
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()