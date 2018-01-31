import random

eyes = [':', ';', '=']
nose = ['-', '^']
mouth = ['D', 'o', 'p', ')', '(']


i = 0
while i < 5:
    emote = random.choice(eyes)
    emote1 = random.choice(nose)
    emote2 = random.choice(mouth)

    x = emote + emote1 + emote2

    print(x)
    i += 1

