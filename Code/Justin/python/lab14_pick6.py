import random

def pick6():
    # Makes a simple list of 6 random integers
    l = []
    for i in range(6):
        l.append(random.randint(1,100))
    return l

def compare (m, w):
    # Compares 2 lists by index.
    # Counts and returns number of matches. match must be in same index
    count = 0
    for i in range(6):
        if m[i] == w[i]:
            count += 1
    return count



awards = [0, 4, 7, 100, 50000, 1000000, 25000000] # Possible awards, index correspondes to number of matches
wins = [0, 0, 0, 0, 0, 0, 0] # Accumulates number of games won, by number of matches
losses = 0 # Accumulates lost dollars
winnings = 0 # Accumulates won dollars



# Loop plays multilple games
# Picks new winning numbers and player ticket each game
# Accumulates number of wins, total winnings and total losses, $2 per game
for i in range(100000):
    print(i)
    my_ticket = pick6() # Get player ticket
    print(my_ticket)
    losses -= 2 # Accumulate dollar losses
    winning_numbers = pick6() # Get winning numbers
    print(winning_numbers)
    matches = compare(my_ticket, winning_numbers)
    wins[matches] += 1 # Accumulate number of games with each number of matches
    winnings += awards[matches] # Accumulate dollars won
    if matches > 0:
        print(f'You won ${awards[matches]} with {matches} matches!!!') # Print congratualtory message
        print('*' * 30 + '*' * 20 * matches) # Visiual indicator of won game
    else:
        print('Better luck next time :(')

print('Number of matches 0 - 6: ', wins)
print('Dollar losses: ', losses)
print('Dollar winnings: ', winnings)
print('ROI: ', (winnings - losses) / losses)
