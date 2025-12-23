from stats import word_count, text_dict, sort_dict, sort_on
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text(book_path):

    with open(book_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents



def main():

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = word_count(text)
    num_letters = text_dict(text)
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...""")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    letter_dict = sort_dict(num_letters)
    for key in letter_dict:
        char = key["char"]
        num = key["num"]
        if char.isalpha():
            print(f"{char}: {num}")
        else:
            continue
    print("============= END ===============")
    

main()


