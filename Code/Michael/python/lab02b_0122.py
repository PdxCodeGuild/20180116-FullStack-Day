# Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas,
# then use the .split() function to store each adjective and later use it in your story.

# Add randomness! Use the random module, rather than selecting which adjective goes where in the story.

import random

adjective1 = str(input('Type first adjective. '))
adjective2 = str(input('Type second adjective. '))
adjective3 = str(input('Type third adjective. '))

verb1 = str(input('Type first verb. '))
verb2 = str(input('Type second verb. '))
verb3 = str(input('Type third verb. '))

noun1 = str(input('Type first noun. '))
noun2 = str(input('Type second noun. '))
noun3 = str(input('Type third noun. '))

adjectives = [adjective1, adjective2, adjective3]
verbs = [verb1, verb2, verb3]
nouns = [noun1, noun2, noun3]


print(f'{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)} were {random.choice(verbs)} together over a {random.choice(nouns)} of a year, {random.choice(verbs)} the name of a {random.choice(nouns)} {random.choice(verbs)} the changes between {random.choice(nouns)}.')