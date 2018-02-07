import random
number_count = 0
lucky = []
while True and number_count < 6: #ensuring no strings are added to the list of numbers
    try:
        user = int(input("Let's pick some numbers.\n0 to 99?\n:"))
        lucky.append(user)
        number_count += 1
        continue
    except ValueError:
        continue
balance = 0
game_count = 0


while game_count < 100000:
    balance -= 2
    com_ticket = []
    for i in range(6):
        com_ticket.append(random.randint(0, 99))
    print(com_ticket)
    print(lucky)

    i = 0
    matches = 0
    while i < 6:
        if com_ticket[i] == lucky[i]:
            matches += 1
        i += 1
    winnings = {0: 0, 1: 4, 2: 7, 3: 100, 4: 5000, 5: 1000000, 6: 25000000}
    balance += winnings[matches]


    game_count += 1
if balance > 0:
    print(f'''You have won ${balance}.''')
if balance < 0:
    print(f'''You owe ${balance}.''')
expenses = 2 * 100000
earnings = balance - expenses
ROI = earnings / expenses
print(f'''Your ROI is {ROI}.''')









