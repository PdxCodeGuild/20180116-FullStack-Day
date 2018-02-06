#  ANAGRAMMER
user_anagram1 = input('hello! i am the anagrammer!\ni can tell you what words or phrases are or are not '
                      'anagrams!\nplease enter a word or phrase you would like to compare\n\n:')

user_anagram2 = input('okay! now what word or phrase would you like to compare to and check for an anagram?\n\n:')


def anagrammer(user_anagram1, user_anagram2):
	user_anagram1 = user_anagram1.lower()
	user_anagram2 = user_anagram2.lower()
	user_anagram1 = user_anagram1.replace(' ', '')
	user_anagram2 = user_anagram2.replace(' ', '')
	return sorted(user_anagram1) == sorted(user_anagram2)


print(anagrammer(user_anagram1, user_anagram2))
