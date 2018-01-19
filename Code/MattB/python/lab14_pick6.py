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


earnings = 0

expenses = 0

winners = pick6()

for x in range(0, 100000):
    hits = 0
    expenses += 2
    picks = pick6()
    hits += check(winners, picks)
    if hits == 0:
        earnings += 0
    elif hits == 1:
        earnings += 4
    elif hits == 2:
        earnings += 7
    elif hits == 3:
        earnings += 100
    elif hits == 4:
        earnings += 50000
    elif hits == 5:
        earnings += 1000000
    elif hits == 6:
        earnings += 25000000

roi = (earnings - expenses) / expenses
print(f'You\'re expenses = {expenses}, earnings = {earnings}, and ROI = {roi}')




