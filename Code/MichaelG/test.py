import random

winno0 = random.randint(1, 99)
winno1 = random.randint(1, 99)
winno2 = random.randint(1, 99)
winno3 = random.randint(1, 99)
winno4 = random.randint(1, 99)
winno5 = random.randint(1, 99)
winno = [winno0, winno1, winno2, winno3, winno4, winno5]
winnostring = str(winno)


i = 0
while i < 100000000:
    myno0 = random.randint(1, 99)
    myno1 = random.randint(1, 99)
    myno2 = random.randint(1, 99)
    myno3 = random.randint(1, 99)
    myno4 = random.randint(1, 99)
    myno5 = random.randint(1, 99)
    yourno = [myno0, myno1, myno2, myno3, myno4, myno5]
    yournostring = str(yourno)
    if (winno[0] - winno[5]) == (yourno[0] - yourno[5]):
        print('asdf')
    i += 1
