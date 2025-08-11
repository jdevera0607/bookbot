import sys
from stats import get_num_words, get_num_char
if len(sys.argv) == 1:
    print("Error! Please try this to use the program")
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    print("Reading book...")
    book = sys.argv[1]
    get_num_words(book)
    print("Complete!")

