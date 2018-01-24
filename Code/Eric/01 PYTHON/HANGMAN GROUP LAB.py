# HANGMAN LAB: ERIC/ MATT/ JACKSON/ ZIXUAN
import random

with open('english.txt', 'r') as wordlist:
	contents = wordlist.read().split('\n')

with open('hangmanpics.txt', 'r') as hangman:
	man_pics = hangman.read()
	man_pics = man_pics.split(',')

word = ''

while len(word) < 5:
	word = random.choice(contents)
	word = word.lower()

print(word)

letters_guessed = []
counter = 0


def replace(word, guessed):
	new_word = ''
	new_word = new_word.lower()
	for i in range(len(word)):
		if word[i] in guessed:
			new_word = new_word + f'{word[i]} '
		else:
			new_word = new_word + '_ '
	print(new_word)
	if '_' not in new_word:
		print('you win!')
		return 'win'
	return new_word


while counter < 10:
	guess = input('guess a letter\n\n:').lower()
	guess = guess.lower()
	while guess in letters_guessed:
		guess = input('already guessed. try again\n:').lower()
		guess = guess.lower()
	letters_guessed.append(guess)
	new = replace(word, letters_guessed)
	new = new.lower()
	if new == 'win':
		break
	if guess not in word:
		counter += 1
		print(man_pics[counter])
		print(f'sorry, wrong guess! you have {10 - counter} guesses remaining ')

if counter == 10:
	print('you are out of guesses! too bad!')
