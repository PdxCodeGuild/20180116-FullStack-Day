change = {'Quarters': 25, 'Dimes': 10, 'Nickels': 5, 'Pennies': 1}
monies = int(input('How much shmeckles?\n:'))
monies1 = monies // change

while monies in change.keys():
    monies = int(input('How much shmeckles?\n:'))
    monies1 = monies // change
print(monies1)


