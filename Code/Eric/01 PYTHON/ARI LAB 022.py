with open('Music as a Language by Ethel Home.txt', 'r') as book:
	book = book.read().lower()

words = list(book.split())

number_of_sentences = len(book.split('. '))
number_of_words = len(words)
number_of_characters = 0

for word in words:
	number_of_characters += len(word)

print('\n# of sentences: ' + str(number_of_sentences))
print('# of words: ' + str(number_of_words))
print('# of characters: ' + str(number_of_characters))

ari = ((4.71 * (number_of_characters / number_of_words)) + (0.5 * (number_of_words / number_of_sentences))) - 21.43

ari = round(ari + 0.49)

print('\nARI score: ' + str(ari))

ari_values = {
	1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
	2: {'ages': '6-7', 'grade_level': '1st Grade'},
	3: {'ages': '7-8', 'grade_level': '2nd Grade'},
	4: {'ages': '8-9', 'grade_level': '3rd Grade'},
	5: {'ages': '9-10', 'grade_level': '4th Grade'},
	6: {'ages': '10-11', 'grade_level': '5th Grade'},
	7: {'ages': '11-12', 'grade_level': '6th Grade'},
	8: {'ages': '12-13', 'grade_level': '7th Grade'},
	9: {'ages': '13-14', 'grade_level': '8th Grade'},
	10: {'ages': '14-15', 'grade_level': '9th Grade'},
	11: {'ages': '15-16', 'grade_level': '10th Grade'},
	12: {'ages': '16-17', 'grade_level': '11th Grade'},
	13: {'ages': '17-18', 'grade_level': '12th Grade'},
	14: {'ages': '18-22', 'grade_level': 'College'}
}

if ari > 14:
	ari = 14
else:
	ari = ari

print(f'\nThe ARI score of Ethel Home\'s "Music as a Language" is: {ari}\n'
      f'This corresponds to a(n) {ari_values[ari]["grade_level"]} level of difficulty\n'
      f'This material is generally recommended for people {ari_values[ari]["ages"]} years of age.')
