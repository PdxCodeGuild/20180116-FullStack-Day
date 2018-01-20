"Lab 14: Pick6"
import random

lottery = []

for i in range(0, 6):
    lotterynumber = random.randint(1, 99)
    lottery.append(lotterynumber)
    i += 1

print('Lottery numbers: ')
print(lottery)

ticket = []

for i in range(0, 6):
    ticketnumber = random.randint(1, 99)
    userticket = input('Enter a number between 1-100 ')
    ticket.append(userticket)
    i += 1

print('Your lottery numbers: ')
print(ticket)

match = 0

def matches(lottery, ticket):
    for i in range(0, 6):
        if lottery[i] == ticket[i]:
            match += 1
#  not done



