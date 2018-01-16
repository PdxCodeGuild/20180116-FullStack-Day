import random
eyes = [':', ';', '8']; nose = ['-', '~', 'o']; mouth =['P', 'D', ')', '(']
print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))

count = 0
while(count < 4):
    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
    count = count + 1
