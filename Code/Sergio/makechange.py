total_cash = float(input('How much money do you have?\n:'))
total_quarters = total_cash / .25
total_dimes = total_cash / .10
total_nickels = total_cash / .05
total_pennies = total_cash / .01

print('quarters: ' + str(total_quarters))
print('dimes: ' + str(total_dimes))
print('nickels: ' + str(total_nickels))
print('pennies: ' + str(total_pennies))
