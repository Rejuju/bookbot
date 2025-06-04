def length_of_book(bookscontents: str)  -> int:
        num_words = len(bookscontents.split())
        return num_words
def number_of_characters(contentsofbook:str) -> dict:
	character_dictionary = {}
	contentsofbook = contentsofbook.lower()
	for character in contentsofbook:
		if character not in character_dictionary:
			character_dictionary[character] = 1
		else:
			character_dictionary[character] += 1
	return character_dictionary
def sorted_number_of_characters(character_dictionary: dict) -> dict:
	list_of_dictionaries = []
	for key,value in character_dictionary.items():
		list_of_dictionaries.append({key: value})
	sorted_list_of_dictionaries = sorted(list_of_dictionaries, key=lambda character: list(character.values())[0],reverse=True)
	return sorted_list_of_dictionaries	
