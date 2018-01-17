"""
Lab 5
Because the world needs more emoticons!
"""

import random

eyes = [':', ':', '=', '<:', '>:', '[:', '{:', 'X', 'O;']
noses = ['-', '>', '^', '=', '~', '', '-']
mouths = ['O', '0', 'o', ')', '(', ']', '}', '%', '#', '@', '*', '|', 'D', 'P']
happy = [')', ']', '}', '*', 'D', 'P']
sad = ['(', '[', '{', '(', '<']
meh = ['O', '0', 'o', '%', '#', '@', '*', '|']

i = 0

print("Here come the emoticons!\n")

while i < 5:
    emoticon = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
    print(emoticon)
    print("")
    i += 1

mood = input("How are you feeling today? ")

if "sad" in mood:
    emoticon = random.choice(eyes) + random.choice(noses) + random.choice(sad)
    print(emoticon)

elif "happy" in mood:
    emoticon = random.choice(eyes) + random.choice(noses) + random.choice(happy)
    print(emoticon)

else:
    emoticon = random.choice(eyes) + random.choice(noses) + random.choice(meh)
    print(emoticon)