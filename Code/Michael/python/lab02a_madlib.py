import random

name = input("> What is your Name? ") # asking name
if name == 'no':
    print('i quit')
    exit(0)

adjective = input("> How do you feel? ") # how are we feeling
if adjective == 'no':
    print('i quit')
    exit(0)

verb = input("> What are we doing? ") # what are we doing
if verb == 'no':
    print('i quit')
    exit(0)

new = (f'Hello, {name} it is {adjective} {verb} with you.')

print(new)

new2 = new.split(' ')

print(new2)

rand = random.choice(new2)
rand2 = random.choice(new2)
rand3 = random.choice(new2)
rand4 = random.choice(new2)
rand5 = random.choice(new2)

print(f'{rand} {rand2} {rand3} {rand4}.')
