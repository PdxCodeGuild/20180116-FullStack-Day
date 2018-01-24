"""
Random Emoticon Generator with while loop to generate 5 emoticons
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

#Assemble and display the emoticon
print(eye+nose+mouth) #first one

#use a while loop to produce 5 emoticons

x = 0
while x < 4: #4 more
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    print(eye + nose + mouth)
    x += 1

