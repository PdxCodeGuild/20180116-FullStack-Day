import random
payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
expense = 0
earnings = 0

m = 0
while m < 100000:
# Winning ticket numbers
    winning_ticket = []

    i = 0
    while i < 6:

        winning_ticket.append(random.randint(1, 99))
        i += 1

    user_ticket = []
    i = 0
    while i < 6:

        user_ticket.append(random.randint(1, 99))

        i += 1
    expense -= 2
    # print(winning_ticket)
    # print(user_ticket)
    #print(f"Your balance is: ${balance}.")

    matches = 0
    for g in range(6):
        if user_ticket[g] == winning_ticket[g]:
            matches = matches + 1


    earnings += (payout[matches]) #test

    m += 1
ROI = (earnings - expense)/expense
print(earnings)
print(expense)
print(ROI)









