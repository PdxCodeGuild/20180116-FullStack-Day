# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
import random

game = 0
bal = 0
winning = []
nikki_six = []
rolling_stone = []

while game < 100000:
    nikki_six = []
    for i in range(0, 6):
        nikki_six.append(random.randint(0, 99))

    rolling_stone = []
    for i in range(0, 6):
        rolling_stone.append(random.randint(0, 99))
    win_count = 0
    for i in range(0, 6):
        if rolling_stone[i] == nikki_six[i]:
            bal -= 2
game += 1

if nikki_six[0] == rolling_stone[0]:
    print('Match')
elif nikki_six[1] == rolling_stone[1]:
    print('match')
elif nikki_six[2] == rolling_stone[2]:
    print('match')
elif nikki_six[3] == rolling_stone[3]:
    print('match')
elif nikki_six[4] == rolling_stone[4]:
    print('match')
elif nikki_six[5] == rolling_stone[5]:
    print('match')
elif nikki_six[6] == rolling_stone[6]:
    print('match')
elif nikki_six[1, 2] == rolling_stone[1, 2]:
    print('two matches')
elif nikki_six[2, 3] == rolling_stone[2, 3]:
    print('match')
print(compare)
print(i)
print(bal)
print(nikki_six)
print(rolling_stone)



