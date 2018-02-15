import random
payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
balance = 0

# Winning ticket numbers
winning_ticket = []

i = 0
while i < 6:
    for i in range(6):
        winning_ticket.append(random.randint(1, 99))
    i += 1

user_ticket = []
i = 0
while i < 6:
    for i in range(6):
        user_ticket.append(random.randint(1, 99))

    i += 1
balance -= 2
print(winning_ticket)
print(user_ticket)
print(f"Your balance is: ${balance}.")


for i in range(6):
    if user_ticket[i] == winning_ticket[i]:
        print('match', user_ticket[i] and winning_ticket[i]) #test







