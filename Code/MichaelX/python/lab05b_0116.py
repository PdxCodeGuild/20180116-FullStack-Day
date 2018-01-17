import random

eye = [';',':','8','E','>']
nose = ['^','-','>','@','7']
mouth = [')','/','D','O','P']

eye.pop
nose.pop
mouth.pop

eyes = random.choice(eye)
noses = random.choice(nose)
mouths = random.choice(mouth)

facia = (f'{eyes}{noses}{mouths}')

while (facia < 5):
    print(facia)
    facia += 1
    print(facia)
