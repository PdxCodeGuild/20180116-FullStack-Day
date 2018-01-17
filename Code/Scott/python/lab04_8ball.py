# print welcome screen
print('Welcome to the magic 8 Ball!')

# import random
import random

# create list
magicball = ['it is certain', 'it is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'Ask again later', 'Don\'t count on it' ]

user_response = True

while user_response != 'no':
    input('Ask me a question and I will tell you your fortune: ')
    print(random.choice(magicball))
    user_response = input('Would you like to play again? ')






