import random

eyes = [':', '=', ';']
noses = ['', '-', '\'', '^', '+']
mouths = [')', ']', '|', '/', '\\', 'D', 'P', '3']

i = 0

while i < 5:
    e = random.choice(eyes)
    n = random.choice(noses)
    l = random.choice(mouths)

    s = e + n + l
    print(s)
    i = i + 1
