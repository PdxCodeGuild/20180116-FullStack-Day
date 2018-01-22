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
    ticket1 = []:
    for number in range(primary_lottery):
        ticket1.append()
    ticket2 = []:
    for number in range(human_ticket)
        ticket2.append()
    if ticket1() == ticket2()
        match = match + 1


# Make primary lottery ticket user is trying to win against.

primary_lottery = pick6()
print(primary_lottery)


# Make a lottery ticket for the human

human_ticket = pick6()
print(human_ticket)

# Run the lottery a set number of times

# Figure out how to make the computer match the numbers in order.
'''
def compare (primary, human):
    count = 0
    for i in range(6):
        if primary[i] == human[i]:
            count = count + 1
    return count

'''

#  Output how many times each $ amount was won.

