"""
Random Emoticon Generator
"""

import random

#Define a list of eyes
eyes = [':', ';', '8']

#Define a list of noses
noses = ['^', '', '~']

#Define a list of mouths
mouths = ['p', '\\', '{']

#Randomly pick a set of eyes
eye = random.choice(eyes)

#Randomly pick a nose
nose = random.choice(noses)

#Randomly pick a mouth
mouth = random.choice(mouths)

#use a while loop to produce 5 emoticons

eye = random.choice(eyes)
nose = random.choice(noses)
mouth = random.choice(mouths)
print(eye + nose + mouth)

