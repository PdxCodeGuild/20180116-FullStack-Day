import random

letters = 'abcdefghijklmnopqrstuvwxyz'

#User input for length of password
n = int(input('How long would you like your password to be?: '))

i = 0
while i < n:
    print(random.choice(letters), end='')
    i += 1