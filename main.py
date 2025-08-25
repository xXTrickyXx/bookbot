
from stats import get_line_count
from stats import get_word_count
import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"Analysing book found at {sys.argv[1]}")
    print("============================================")
    print(get_word_count(sys.argv[1]))
    print("============================================")
    result = get_line_count(sys.argv[1])
    for item in result:
        print(f"{item['char']}: {item['num']}")

main()