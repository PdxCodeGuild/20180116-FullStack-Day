import random

eye = ['1', '2', '3']
nose = ['a', 'b', 'c']
leg = ['A', 'B', 'C']

i = 0

while i < 5:
    e = random.choice(eye)
    n = random.choice(nose)
    l = random.choice(leg)

    s = e + n + l
    print(s)
    i = i + 1
