import random


##############################################################
# Picks six random numbers when called
###############################################################
def pick6():
    number = [random.randrange(1, 100), random.randrange(1, 100),
                        random.randrange(1, 100), random.randrange(1, 100),
                        random.randrange(1, 100), random.randrange(1, 100)]
    return number

##############################################################
#
###############################################################
def num_matches(winning, ticket):
    count = 0
    i = 0
    while i < len(winning):
        if winning[i] == ticket[i]:
            count += 1
            i += 1
        else:
            i += 1

    return count




# Prize Amount has the prizes won for every match you have
prize_amount = {1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
i = 0
balance = 0
ticket_price = 2

total_expense = 0

while i < 100000:

    computer_pick = pick6()
    user_pick = pick6()
    count = num_matches(computer_pick, user_pick)

    if count == 0:
        total_expense += ticket_price
    else:
        balance += prize_amount[count]
        total_expense += ticket_price

    i += 1

print(f'The balance is ${balance - total_expense}.')
print(f'Total amount of ROI is: %{100 * (balance - total_expense) / total_expense}')



