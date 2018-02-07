import random

times = 0
amount=0
while times < 100000:
    win = []
    for i in range(0, 6):
        win.append(random.randint(1, 10))

    ticket = []

    for x in range(6):
        ticket.append(random.randint(1, 10))
    winnumber = 0

    for y in range(0, 6):
        if win[y] == ticket[y]:
            winnumber += 1

    win_money = 0
    if winnumber == 1:
        win_money = 4
    elif winnumber == 2:
        win_money = 7
    elif winnumber == 3:
        win_money = 100
    elif winnumber == 4:
        win_money = 50000
    elif winnumber == 5:
        win_money = 1000000
    elif winnumber == 6:

        win_money = 25000000

    amount += win_money

    times = times + 1

print("amount of money win is "+str(amount))
print("amount of money cost is " + str(200000))
print("ROI=" + str((amount-200000)/200000))