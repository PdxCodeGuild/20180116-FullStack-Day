import random

eyes = [':', ';', '{']
noses = ['-', '*', '=']
mouths = ['$', '%', '/', '*', ')', '(', 'P', '#']

i = 0
while i < 5:
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    emoji = eye + nose + mouth
    print(emoji)
    i += 1
