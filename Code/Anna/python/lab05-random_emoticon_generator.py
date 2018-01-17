"""
Lab 5
Because the world needs more emoticons!
"""
import random

eyes = [':', ':', '=', '<:', '>:', '[:', '{:', 'X', 'O;']
noses = ['-', '>', '^', '=', '~', '', '-']
mouths = ['O', '0', 'o', ')', '(', ']', '}', '%', '#', '@', '*', '|', 'D', 'P']

i = 0

print("Here come the emoticons!\n")

while i < 5:
    emoticon = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
    print(emoticon)
    print("")
    i += 1
