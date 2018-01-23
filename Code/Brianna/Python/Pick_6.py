# Pick numbers
import random

# Make a way to create a lottery ticket and/or lottery answer
def pick6():
    lottery = []
    for i in range(6):
       lottery.append(random.randint(0, 100))
    return lottery

# Make a comparison function
def compare(primary_lottery, human_ticket)
    match = 0
    for i in range(len(primary_lottery)):
        if primary_lottery[i] == human_ticket[i]:
            match += 1
    return match


# Make primary lottery ticket user is trying to win against.

primary_lottery = pick6()
print("The winning ticket is: " + primary_lottery)


# Make a lottery ticket for the human

human_ticket = pick6()
print("Your ticket was " + human_ticket)

balance = 0



'''
a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance

'''