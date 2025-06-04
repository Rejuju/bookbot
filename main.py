from stats import length_of_book
from stats import number_of_characters
from stats import sorted_number_of_characters
import sys

if len(sys.argv) != 2:
	print(f"Usage: python3 main.py <path_to_book>")
	sys.exit(1)
else:
	path_to_bookfile = sys.argv[1]

def get_book_text(filepath: str) ->str: 
	with open(filepath) as f:
		 file_contents = f.read()
	return file_contents

def main():
	file_contents = get_book_text(path_to_bookfile)
	character_dictionary = number_of_characters(file_contents)
	sorted_character_dictionary =  sorted_number_of_characters(character_dictionary)

	print(f"============ BOOKBOT ============\n Analyzing book found at books/frankenstein.txt...\n ----------- Word Count ----------\n Found {length_of_book(file_contents)} total words \n --------- Character Count -------\n")
	for entry in sorted_character_dictionary:
		key = list(entry.keys())[0]
		value = list(entry.values())[0]
		if key.isalpha():
			print(f"{key}: {value}\n")
	print("============= END ===============")
main()
