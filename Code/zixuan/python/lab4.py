import random
a="1,2,3,4,5,6,7,8,9,10"
b = random.choice(a)
a=int(input('input a number between 1-10:'))

if a == b:
    print('you are win')
else:
    print('win number is ' + b)
