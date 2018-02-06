import time
import random

roll = ['scissors', 'paper', 'rock']

throw = random.choice(roll) #comp's choice

print('Hello')
print('Will you choose')
print('Rock')
print('Paper')

pchoice = input('Or Scissors? ')
output = 'You have chosen ' + pchoice #your choice
print(output)
print('I choose...')
time.sleep(0.5)
print(throw)

if pchoice == throw:
    print('Tie!')
elif pchoice == 'rock' and throw == 'scissors':
    print('You win!')
elif pchoice == 'rock' and throw == 'paper':
    print('You lose!')
elif pchoice == 'paper' and throw == 'scissors':
    print('You lose!')
elif pchoice == 'paper' and throw == 'rock':
    print('You win!')
elif pchoice == 'scissors' and throw == 'paper':
    print('You win!')
elif pchoice == 'scissors' and throw == 'rock':
    print('You lose!')







# cover the other cases