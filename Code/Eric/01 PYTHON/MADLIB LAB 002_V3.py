#MADLIB GAME V3: (NOW WITH REPETITION!)

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

plural_nouns = random.choice(plural_nouns)
plural_nouns = str(random.choice(plural_nouns))

#STORY
story = story.lower
story.lower = input('\nWould you like to read your story??? Type "Yes" or "No"\n:')
while True:
	if story.lower is 'Yes':
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
			'Or you can save your ' + random.choice(plural_nouns) + ' for another time!\n\n:'
			'(source link: http://www.teach-nology.com/worksheets/language_arts/madlibs/3/)')
		again_1 = again_1.lower
		again_1.lower = input('\nWould you like to read the story  again??? Type "Yes" or "No"\n:')
		while True:
			if again_1.lower is 'Yes':
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
					'Or you can save your ' + random.choice(plural_nouns) + ' for another time!\n\n:'
					'(source link: http://www.teach-nology.com/worksheets/language_arts/madlibs/3/)')
			elif again_1 is 'no':
				another_story1 = another_story1.lower
				another_story1.lower = input('\nWould you like to make another story?? Type "Yes" or "No"\n:')
				while True:
					if another_story1.lower is 'Yes':
						plural_nouns = input('Please provide four(4) plural nouns, properly separated by commas\n:'
					if another_story1.lower is 'No':
						print('\nThank you for playing! Goodbye!'
					else:
						print('Please answer with "Yes" or "No"...\n')
						another_story1.lower = input('\nWould you like to make another story??\n:')
	elif story.lower is 'no':
	another_story2 = another_story2.lower
	another_story2.lower = input('\nWould you like to make another story?? Type "Yes" or "No"\n:')
	while True:
		if another_story2.lower is 'Yes':
			plural_nouns = input('Please provide four(4) plural nouns, properly separated by commas\n:'
		elif another_story2.lower is 'no':
			print('\nThank you for playing! Goodbye!')
		else:
			print('Please answer with "Yes" or "No"...\n')
			another_story2.lower = input('\nWould you like to make another story??\n:')
			print("Thank you for playing! Goodbye!")
			break
	else:
		print('Please answer with "Yes" or "No"...\n')
		story.lower = input('\nWould you like to read your story??? Type "Yes" or "No"\n:')

#COME BACK TO THIS