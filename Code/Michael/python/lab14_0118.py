import random

def lottery():

    ticket = []
    megabucks = list(range(1, 48))
    i = 0

    while i < 6:
        i += 1
        random.shuffle(megabucks)
        nums = megabucks.pop()
        ticket.append(nums)
    ticket.sort()

    return ticket


tot_wins = [0, 0, 0, 0, 0, 0]
games = 0
account = 0

while games < 1000000:

    games += 1
    account -= 1
    me = lottery()
    cpu = lottery()
    matches = 0
    win_list = [0, 0, 1, 40, 800, 6800000]
    one = 0

    numbered = 0
    while numbered < 6:
        if me[numbered] == cpu[numbered]:
            matches += 1
        numbered += 1

    if matches > 1:
        account += win_list[matches]

    tot_wins[matches] += 1

print(f'You have {account} dollars!')
for i in range(len(tot_wins)):
    print(i, tot_wins[i])