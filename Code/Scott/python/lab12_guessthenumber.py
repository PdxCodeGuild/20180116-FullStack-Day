#import random
import random

print('Lets play \'Guess the random number\'!')

user_guess = input('Pick a number 1-10: ')
x = random.randint(1,10)
print(x)
i = 1

while i < 10:
    if x == user_guess:
        print('You got it!')
        break
        print('You\'re done son. You\'re done.')
    elif x != user_guess:
        input('Guess again! ')
        x = random.randint(1,10)
        print(x)
    i += 1
print('You\'re done son. You\'re done.')

