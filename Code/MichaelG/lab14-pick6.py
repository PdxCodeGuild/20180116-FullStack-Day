import random
# Winning ticket numbers
winno0 = random.randint(1, 99)
winno1 = random.randint(1, 99)
winno2 = random.randint(1, 99)
winno3 = random.randint(1, 99)
winno4 = random.randint(1, 99)
winno5 = random.randint(1, 99)
winno = [winno0, winno1, winno2, winno3, winno4, winno5]
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
while i < 100000:
    # Your ticket numbers
    myno0 = random.randint(1, 99)
    myno1 = random.randint(1, 99)
    myno2 = random.randint(1, 99)
    myno3 = random.randint(1, 99)
    myno4 = random.randint(1, 99)
    myno5 = random.randint(1, 99)
    yourno = [myno0, myno1, myno2, myno3, myno4, myno5]
    yournostring = str(yourno)
    results = (set(winno) & set(yourno))
    result = str(results)

    if (winno[0]) == (yourno[0]):
        print('*| | | | | ')
        if (winno[0] and winno[1]) == (yourno[0] and yourno[1]):
            print('*|*| | | | ')
            if (winno[0] and winno[1] and winno[2]) == (yourno[0] and yourno[1] and yourno[2]):
                print('*|*|*| | | ')
                if (winno[0] and winno[1] and winno[2] and winno[3]) == (
                        yourno[0] and yourno[1] and yourno[2] and yourno[3]):
                    print('*|*|*|*| | ')
                    if (winno[0] and winno[1] and winno[2] and winno[3] and winno[4]) == (
                            yourno[0] and yourno[1] and yourno[2] and yourno[3] and yourno[4]):
                        print('*|*|*|*|*| ')
                        if (winno[0] and winno[1] and winno[2] and winno[3] and winno[4] and winno[5]) == (
                                yourno[0] and yourno[1] and yourno[2] and yourno[3] and yourno[4] and yourno[5]):
                            print('*|*|*|*|*|*')
        if (winno[1]) == (yourno[1]):
            print(' |*| | | | ')
            if (winno[1] and winno[2]) == (yourno[1] and yourno[2]):
                print(' |*|*| | | ')
                if (winno[1] and winno[2] and winno[3]) == (yourno[1] and yourno[2] and yourno[3]):
                    print(' |*|*|*| | ')
                    if (winno[1] and winno[2] and winno[3] and winno[4]) == (
                            yourno[1] and yourno[2] and yourno[3] and yourno[4]):
                        print(' |*|*|*|*| ')
                        if (winno[1] and winno[2] and winno[3] and winno[4] and winno[5]) == (
                                yourno[1] and yourno[2] and yourno[3] and yourno[4] and yourno[5]):
                            print(' |*|*|*|*|*')
                            if (winno[2]) == (yourno[2]):
                                print(' | |*| | | ')
                                if (winno[3]) == (yourno[3]):
                                    print(' | | |*| | ')
                                    if (winno[4]) == (yourno[4]):
                                        print(' | | | |*| ')
                                        if (winno[5]) == (yourno[5]):
                                            print(' | | | | |*')
    i += 1





