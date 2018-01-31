import random

welcome = input('Would you like a password?')
while True:

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCD012346789'
    output = ''
    output += random.choice(alphabet)
    output += random.choice(alphabet)
    output += random.choice(alphabet)
    output += random.choice(alphabet)
    output += random.choice(alphabet)
    output += random.choice(alphabet)
    if welcome == 'yes':
        print('Creating password')
        print(output)
        welcome = input('Would you like another password?')

    else:
        break


print('Thank you.')
