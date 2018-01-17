import random

eye = [';',':','8','3']
nose = ['^','-','>','@']
mouth = [')','/','|','D','O','P']

eyes = random.choice(eye)
noses = random.choice(nose)
mouths = random.choice(mouth)

print(f'{eyes}{noses}{mouths}')