from stats import get_num_words, get_chars, create_list
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words = get_num_words(book_text)
    char_count = get_chars(book_text)
    final_list = create_list(char_count)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

      
    for i in final_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")

main()

 
