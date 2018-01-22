import random

win = []
for i in range(0 ,6):
    win.append(random.randint(1, 10))

print(str(win))
ticket = []

for x in range(6):
    ticket.append(random.randint(1, 10))
print(str(ticket))
winnumber = 0

for y in range (0, 6):

    if win[y] == ticket[y]:
        winnumber += 1


print(winnumber)
