def make_change():
    change = int(input('Please enter the amount of change:'))
    print(change // 25, "quarters")
    change = change % 25
    print(change // 10, "dimes")
    change = change % 10
    print(change // 5, "nickles")
    change = change % 5
    print(change // 1, "pennies")


make_change()

