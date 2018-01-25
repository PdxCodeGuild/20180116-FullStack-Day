# Pick 6
#
# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
import random


def main():
    wins = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}  # hits: payout on win
    bal = 0  # init balance
    print('Starting balance is $', bal)
    plays = 0
    tot_matches = 0
    expenses = 0
    earnings = 0
    while plays < 100000:
        plays += 1
        your_nums = []
        check_nums = []
        for i in range(6):
            your_nums.append(random.randint(0, 99))
            check_nums.append(random.randint(0, 99))
        bal -= 2
        expenses += 2
        print('Your six numbers are', your_nums)
        print('The winning list is', check_nums)
        hits = 0
        i = 0
        while i < 5:  # iterate through list 1.
            if your_nums[i] == check_nums[i]:
                print('got one!!')
                hits += 1
                tot_matches += 1
            i += 1
        bal += wins.get(hits)
        earnings += wins.get(hits)

    print('Played ', plays, ' times')
    print('Total match sets attempted: ', tot_matches)
    print('Current balance: $', bal)
    print('Total earnings: $', earnings)
    print('Total expenses accrued: $', expenses)
    print('Accrued ROI value: ', (earnings - expenses) / expenses)


main()
