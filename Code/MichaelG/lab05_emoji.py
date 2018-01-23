import random

eyes = [':', ';', '=']
nose = ['-', '^']
mouth = ['D', 'o', 'p', ')', '(']

emote = random.choice(eyes)
emote1 = random.choice(nose)
emote2 = random.choice(mouth)

x = ((emote) + (emote1) + (emote2))

i = 0
while i < 5:
    print(x)
    i += 1