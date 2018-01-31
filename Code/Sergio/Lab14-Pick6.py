"Lab 14: Pick6"
import random

ticket_values = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}

# computer generated lottery 'winning' numbers
def computer_choice():
    nums = []
    for i in range(6):
        num = random.randint(1, 99)
        nums.append(num)
    return nums
winning_ticket = computer_choice()

print('::::LOTTERY NUMBERS:::: ')
print(winning_ticket)

# generates user ticket numbers
def pick6():
    nums = []
    for i in range(6):
        num = random.randint(1, 99)
        nums.append(num)
    return nums


def find_matches(lottery_nums, ticket_nums):
    matches = 0
    for i in range(0, 6):
        if lottery_nums[i] == ticket_nums[i]:
            matches += 1
    #print(f'matches: {matches}')
    print(ticket_values[matches])
    return ticket_values[matches]


balance = 0

for i in range(100000):  # 100,000 tickets
    balance -= 2
    user_ticket = pick6()
    print('Your ticket numbers: ')
    print(user_ticket)
    balance += find_matches(winning_ticket, ticket_values)

print(balance)

