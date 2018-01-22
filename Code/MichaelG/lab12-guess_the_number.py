import random


print('I am thinking of a number between 1 and 10.')
print('You have 10 tries to guess it right')
x = random.randint(1, 10)
i = 0
while i < 10:
    guess = input('Enter your number: ')
    y = int(guess)
    r = str(i + 1)
    if y == x:
        print('Congratulations! You guessed ' + r + ' times.')
        break
    elif y != x:
        print('Try again')
        i += 1

print('Thank you for playing.')
