import random
# Winning ticket numbers






winnostring = str(winno)

# Payout in $
one_match = +4
two_matches = +7
three_matches = +100
four_matches = +50000
five_matches = +1000000
six_matches = +25000000

print('The winning numbers are: ' + winnostring)
print('*|*|*|*|*|*')

i = 0
while i < 100:
    indexwin = 0
    while indexwin < 6:
        winnou.append(random.randint(1, 99))
        indexwin + 1

    # Your ticket numbers
    yourno0 = random.randint(1, 99)
    yourno1 = random.randint(1, 99)
    yourno2 = random.randint(1, 99)
    yourno3 = random.randint(1, 99)
    yourno4 = random.randint(1, 99)
    yourno5 = random.randint(1, 99)
    yourno = [yourno0, yourno1, yourno2, yourno3, yourno4, yourno5]
    yournostring = str(yourno)

    i += 1

    comindex = 0
    while comindex < 6:
        if (yourno[comindex]) == (winno[comindex]):










