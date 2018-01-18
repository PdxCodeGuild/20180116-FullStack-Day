import random


def pick6():
    nums = []
    for num in range(0, 6):
        nums.append(random.randint(0, 99))
    return nums


def check(list1, list2):
    count = 0
    for i in range(0, 6):
        if list1[i] == list2[i]:
            count += 1
        else:
            count += 0
    return count


balance = 0

winners = pick6()

for x in range(0, 100000):
    hits = 0
    balance -= 2
    picks = pick6()
    hits += check(winners, picks)
    if hits == 0:
        balance += 0
    elif hits == 1:
        balance += 4
    elif hits == 2:
        balance += 7
    elif hits == 3:
        balance += 100
    elif hits == 4:
        balance += 50000
    elif hits == 5:
        balance += 1000000
    elif hits == 6:
        balance += 25000000

print(balance)




