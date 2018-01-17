import random

eyes = [':', '8', ';']
nose = ['3', '>', 'o']
mouth = ['/', ')', '(', '()']

i = 0


while i < 5:
    i += 1
    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
else:
    print('143')

