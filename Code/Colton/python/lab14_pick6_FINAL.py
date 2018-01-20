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
    com_1 = random.randint(0, 99)  # I am sure there is a better wat to do lines 4 - 10
    com_2 = random.randint(0, 99)
    com_3 = random.randint(0, 99)
    com_4 = random.randint(0, 99)
    com_5 = random.randint(0, 99)
    com_6 = random.randint(0, 99)
    com = [com_1, com_2, com_3, com_4, com_5, com_6]
    print(com)
    print(lucky)

    i = 0
    matches = 0
    while i < 6:
        if com[i] == lucky[i]:
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
ROI = (earnings - expenses)/expenses
print(f'''Your ROI is {ROI}.''')









