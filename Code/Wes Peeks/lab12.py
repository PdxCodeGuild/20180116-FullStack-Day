import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
comp = random.choice(numbers)
player1 = int(input('Guess a number between 1-10.\n:'))

if player1 == comp:
        print('YAY')
else:
    print('Wrong')

