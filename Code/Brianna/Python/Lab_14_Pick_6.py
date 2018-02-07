# Pick numbers
import random

# Make a way to create a lottery ticket and/or lottery answer
def pick6():
    lottery = []
    for i in range(6):
       lottery.append(random.randint(0, 100))
    return lottery

# Make a comparison function
def compare(primary_lottery, human_ticket):
    match = 0
    for i in range(len(primary_lottery)):
        if primary_lottery[i] == human_ticket[i]:
            match = match + 1
    return match

balance = 0
game = 0


lottery_winnings = {0 : 0, 1 : 4, 2 : 7, 3 : 100, 4 : 50000, 5 : 1000000, 6 : 25000000}

while game < 200:
    primary_lottery = pick6()
    print("lottery numbers", primary_lottery)
    human_ticket = pick6()
    print("your ticket" ,human_ticket)
    balance = balance -2
    match = compare(primary_lottery, human_ticket)
    #print('match',match)
    balance = balance + lottery_winnings[match]
    #print('balance',balance)
    game = game + 1
    #print('game',game)

print("You monnies are now....", balance, "!")
if balance < 0:
    print("Ouch! That hurt!")