"""
Lab 14
Proving that the lottery is a tax on the stupid!
"""

import random


def comp_pick6():
    lottery = []
    for i in range(1, 7):
        lottery.append(random.randint(1, 99))
        i += 1
    print(f"The computer picks: {lottery}")
    return lottery


def human_pick6():
    lottery = []
    global money
    global expenses
    money -= 2
    expenses -= 2

    for i in range(1, 7):
        lottery.append(random.randint(1, 99))
        i += 1
    print(f"The dumb human picks: {lottery}")
    print(f"The human now has ${money}")
    return lottery


def num_matches(winning, ticket):
    global money
    match = 0 # return at end of function!
    for x in range(0, 6):
        if winning[x] == ticket[x]:
            match += 1
    return match


money = 0
expenses = 0
earnings = 0

i = 0
for i in range(0, 100000):
    comp = comp_pick6()
    human = human_pick6()
    i += 1
    matches = num_matches(comp, human)
    if matches == 6:
        print("Winner winner, 25 million chicken dinners!\n")
        money += 25000000
        earnings += 25000000
    elif matches == 5:
        print("You win $1,000,000! Whoo-hoo!\n")
        money += 1000000
        earnings += 1000000
    elif matches == 4:
        print("You win $500,000! Quit your job!\n")
        money += 50000
        earnings += 50000
    elif matches == 3:
        print("You win $100! Not bad.\n")
        money += 100
        earnings += 100
    elif matches == 2:
        print("You win $7! That's a beer.\n")
        money += 7
        earnings += 7
    elif matches == 1:
        print("You win $4! Yay?\n")
        money += 4
        earnings += 4
    else:
        print("Well that was a waste of $2")

print(f"\n\nYou spent ${abs(expenses)} playing the lottery.")
print(f"You won a total of ${earnings}")

ROI = (earnings - expenses)/expenses

print(f"Your return on investment is: {ROI}")

if expenses > earnings:
    print("Wow, you beat the system! Good job!")
else:
    print("Maybe you should put that money in a savings account next time...")