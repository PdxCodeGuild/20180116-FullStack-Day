import random

eye = [';', ':', '8', 'E', '>']
nose = ['^', '-', '>', '@', '7']
mouth = [')', '/', 'D', 'O', 'P']

faces = 0
while faces < 5:
    faces += 1
    eyes = random.choice(eye)
    noses = random.choice(nose)
    mouths = random.choice(mouth)
    print(eyes + noses + mouths)

