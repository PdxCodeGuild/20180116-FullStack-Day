
import random

earnings = 0 #this is for the ROI calculation
total_winnings = 0 #Start your balance at 0
winning_numbers = []

i =0
while i < 6:
    x = random.randint(1, 99)
    winning_numbers.append(x)
    i += 1

# print(winning_numbers) #check

for j in range(100000):
    #Generate a list of 6 random numbers representing the winning numbers
    k = 0
    my_numbers = []
    #Generate a ticket with 6 winning numbers
    while k < 6:
        x = random.randint(1, 99)
        my_numbers.append(x)
        k += 1
    #print(my_numbers) #check
    total_winnings -= 2

    #check to see if won and determine how much to give back
    n = 0
    z = 0 #number of matches on a single ticket
    winning_key = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}
    while n < 6:
        if my_numbers[n] == winning_numbers[n]:
            z += 1
        n += 1
    winnings = winning_key[z]
    earnings += winnings
    total_winnings += winnings

print('earnings:$' + str(earnings))
print('net:$' + str(total_winnings))

#calculate ROI: (earnings - expenses)/expenses
expenses = 2 * 100000
ROI = (earnings - expenses) /expenses
print('ROI:' + str(ROI))