import random

# define lists for eyes, noses, and mouths

eyes = [':', ';', '8']
noses = ['^', '-']
mouths = [')', '(', 'D', 'P']

# randomly pick eyes, nose, and mouth
# print the emoticon output

counter = 1
while counter < 6:
    counter += 1
    print(random.choice(eyes) + random.choice(noses) + random.choice(mouths))

