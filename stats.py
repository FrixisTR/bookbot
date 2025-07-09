def get_num_words(string_file):
	num_of_words = len(string_file.split())
	return num_of_words

def letter_dictionary(string_file):
	letter_amt = {}
	for i in string_file.lower():
		if i.isalpha() == True:
			if i not in letter_amt:
				letter_amt[i] = 1
			else:
				letter_amt[i] += 1
	return letter_amt

def sort_list(dictionary):
	new_list = []
	for i in dictionary:
		new_list.append({"lett": i, "num": dictionary[i]})
	return new_list

def sort_on(items):
	return items["num"]
