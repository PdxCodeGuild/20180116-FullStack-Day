import random
#for i in range(0, 6):
   # com = random.randint(0, 99)
com_1 = random.randint(0, 99) #I am sure there is a better wat to do lines 2 - 8
com_2 = random.randint(0, 99)
com_3 = random.randint(0, 99)#
com_4 = random.randint(0, 99)
com_5 = random.randint(0, 99)
com_6 = random.randint(0, 99)
com = [com_1, com_2, com_3, com_4, com_5, com_6]
count = 0
lucky = []
while True and count < 6:
    try:
        user = int(input("Let's pick some numbers.0 to 99?\n:"))
        lucky.append(user)
        count += 1
        continue
    except ValueError:
        continue
    else:
        break
win = 0
if com[0] == lucky[0]: #used all if so it would all add together, using elif was ineffective
    win += 1
if com[1] == lucky[1]:
    win += 1
if com[2] == lucky[2]:
    win += 1
if com[3] == lucky[3]:
    win += 1
if com[4] == lucky[4]:
    win += 1
if com[5] == lucky[5]:
    win += 1
else:
    print("You didnt match any")

match_1 = 4
match_2 = 7
match_3 = 100
match_4 = 50000
match_5 = 1000000
match_6 = 25000000
if win == 1:
    print(f'''You win ${match_1}.''')
elif win == 2:
    print(f'''You win ${match_2}.''')
elif win == 3:
    print(f'''You win ${match_3}.''')
elif win == 4:
    print(f'''You win ${match_4}.''')
if win == 5:
    print(f'''You win ${match_5}.''')
elif win == 6:
    print(f'''You win ${match_6}.''')


print(win)

print(com)
print(lucky)







