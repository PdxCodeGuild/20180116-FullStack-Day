import random
a=['1','2','3']
b = random.choice(a)
c = input('input a number between 1-10:')

if c == b:
    print('you are win')
    print(1)
else:
    print('win number is ' + b)

