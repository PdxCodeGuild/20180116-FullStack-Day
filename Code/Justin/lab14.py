import random

def pick6():
    l = []
    for i in range(6):
        l.append(random.randint(1,100))
    return l

def compare (m, w):
    count = 0
    for i in range(6):
        if m[i] == w[i]:
            count += 1
    return count



awards = [4, 7, 100, 50000, 1000000, 25000000]
losses = 0
winnings = 0
won_games = []
for i in range(100000):
    print(i)
    my_ticket = pick6()
    print(my_ticket)
    losses -= 2
    winning_numbers = pick6()
    print(winning_numbers)
    matches = compare(my_ticket, winning_numbers)
    if matches > 0:
        print(f'You won ${awards[matches-1]} with {matches} matches')
        print('*' * 50)
        winnings += awards[matches - 1]
        won_games.append(i)
    else:
        print('Better luck next time :(')

print('losses: ', losses)
print('winnings: ', winnings)
print('won games: ', won_games)
