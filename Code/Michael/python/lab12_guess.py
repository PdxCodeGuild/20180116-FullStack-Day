import random

guesses = 0
correct = 0

while guesses < 10:

    guess = int(input('> guess the number?\n> '))

    guesses += 1

    x = random.randint(1, 10)

    if guess == x:
        correct += 1
        print('correct')

    else:
        print('try again!')

print(f'You got {correct} correct!')

