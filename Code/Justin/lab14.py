import random

def pick6():
    # Makes a simple list of 6 random integers
    l = []
    for i in range(6):
        l.append(random.randint(1,100))
    return l

def compare (m, w):
    # Compares 2 lists by index.
    # Counts and returns number of matches.
    count = 0
    for i in range(6):
        if m[i] == w[i]:
            count += 1
    return count



awards = [4, 7, 100, 50000, 1000000, 25000000]
losses = 0
winnings = 0
wins = 0


# Loop plays multilple games
# Picks new winning numbers and player ticket each game
# Accumulates number of wins, total winnings and total losses, $2 per game
for i in range(10000):
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
        wins += 1
    else:
        print('Better luck next time :(')

print('wins: ', wins)
print('losses: ', losses)
print('winnings: ', winnings)

