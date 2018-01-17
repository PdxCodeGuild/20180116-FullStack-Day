import random
from time import sleep

#user = input('What is your name? ')
#print('Welcome, ' + user + '\'!')

PREDICTIONS = ['It is certain', 'It is decidecly so', 'Without a doubt', 'Yes, definitely',
               'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
               'Yes', 'signs point to yes', 'Reply hazy. Try again', 'Ask again later.',
               'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again.',
               'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not good',
               'Very doubtful']


answer = print('Will I win the lottery tomorrow?'), sleep(1), input('Press enter to ask the magic 8 ball.')

print('The magic 8 ball says, ',), sleep(1), print(random.choice(PREDICTIONS) + '!', '\n')