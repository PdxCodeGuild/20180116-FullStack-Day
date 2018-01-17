#MADLIB GAME V2: (LISTS, SPLITS, & RANDOMIZATION)

import random

#LISTS
plural_nouns = []
single_nouns = []
verbs = []

print('Hello! Lets play madlilbs at the arcade! I just need 9 words!')

#WORD REQUESTS
plural_nouns = input('Please provide four(4) plural nouns, properly separated by commas\n:')
while True:
	if ', ' not in plural_nouns:
		print('Please use commas appropriately in your answer\n')
		plural_nouns = input('Please provide four(4) plural nouns, properly separated by commas\n:')
	else:
		plural_nouns = plural_nouns.split(', ')
		plural_nouns.append(plural_nouns)
		break

single_nouns = input('\nPlease provide the name of a comic or cartoon and two(2) singular nouns, properly separated by commas\n:')
while True:
	if ', ' not in single_nouns:
		print('Please use commas appropriately in your answer\n')
		single_nouns = input('\nPlease provide the name of a comic or cartoon and two(2) singular nouns, properly separated by commas\n:')
	else:
		single_nouns = single_nouns.split(', ')
		single_nouns.append(single_nouns)
		break

verbs = input('\nPlease provide a gerundative (-ing) verb and a standard verb, properly separated by commas\n:')
while True:
	if ', ' not in verbs:
		print('Please use commas appropriately in your answer\n')
		verbs = input('\nPlease provide a gerundative (-ing) verb and a standard verb, properly separated by commas\n:')
	else:
		verbs = verbs.split(', ')
		verbs.append(verbs)
		break

print(type(random.choice(plural_nouns)))
print(plural_nouns)
print(type(plural_nouns))

#TEXT
print('When I go to the arcade with my ' + random.choice(plural_nouns) + ', '
	'there are lots of games to play. I spend lots of time there with \n'
	'my friends. In ' + random.choice(single_nouns) +  ', you can be different ' + random.choice(plural_nouns) +
	'. \nThe point of the game is to ' + random.choice(verbs) + ' every bad guy.\n'
	'You also need to save people, and then you can go to the \n'
	'next level. In "Star Wars" you are Luke Skywalker and you try to \n'
	'destroy every' + random.choice(single_nouns) + '. In a car racing / motorcycle \n'
	'racing game you need to beat every computerized vehicle that \n'
	'you are ' + random.choice(verbs) + ' against. There are a whole \n'
	'lot of other cool games. When you play some games you win \n' + random.choice(plural_nouns) +
	' for certain scores. Once youre done, \n'
	'you can cash in your tickets to get a big ' + random.choice(single_nouns) + '!\n'
	'Or you can save your ' + random.choice(plural_nouns) + ' for another time!\n\n:')
	'(source link: http://www.teach-nology.com/worksheets/language_arts/madlibs/3/)')