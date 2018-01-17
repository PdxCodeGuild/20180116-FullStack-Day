import random
eyes = [':', ';', '8']; nose = ['-', '~', 'o']; mouth =['P', 'D', ')', '(']

count = 0
while(count < 5):
    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
    count = count + 1
