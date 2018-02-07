#CHANGE MAKER V2: WE HAVE DOLLAR$ NOW!!!
coin_value = {'dollar':100, 'quarter':25, 'dime':10, 'nickel':5, 'penny':1}
#dollars??
dollars = round(float(input('\nHow many dollars?\n\n:')), 2)

#dollar to pennies
pennies = dollars * 100

#quarters
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

print('\nyou have ' + str(int(quarters)) + ' quarters, ' + str(int(dimes)) + ' dimes, ' + str(int(nickels)) + ' nickels, and ' + str(int(pennies)) + ' pennies.')
