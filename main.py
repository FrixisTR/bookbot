import sys
from stats import get_num_words
from stats import letter_dictionary
from stats import sort_list
from stats import sort_on

if len(sys.argv) < 2: 
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
else:
	path = sys.argv[1]

def main():
	string_file = get_book_text(path)
	num_of_words = get_num_words(string_file)
	num_of_letters = letter_dictionary(string_file)
	sorted_list = sort_list(num_of_letters)
	sorted_list.sort(reverse=True, key=sort_on)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_of_words} total words")
	print("--------- Character Count -------")
	for i in sorted_list:
		char = i["lett"]
		num = i["num"]
		print(f"{char}: {num}")
	print("============= END ===============")
def get_book_text(path):
        with open(path) as f:
                file_contents = f.read()
                return file_contents


main()
