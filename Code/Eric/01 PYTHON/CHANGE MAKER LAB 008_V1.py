#CHANGE MAKER V1: PAYING IN PENNIES
coin_value = {'quarter':25, 'dime':10, 'nickel':5, 'penny':1}

pennies = input('\nhow many pennies?\n\n:')
pennies = int(pennies)

#coin_breakdown
quarters = pennies // 25
remaining = pennies % 25

#dimes
dimes = remaining // 10
remaining = remaining % 10

#nickels
nickels = remaining // (5)
remaining = remaining % (5)

#pennies
pennies = remaining

print('\nyou have ' + str(int(quarters)) + ' quarters, ' + str(int(dimes)) + ' dimes, ' + str(int(nickels)) + ' nickels, and ' + str(int(pennies)) + ' pennies!\ndont spend it all in one place!')