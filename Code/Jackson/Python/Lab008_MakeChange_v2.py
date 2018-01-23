"""
In version 2 we allow the user to input a dollar amount, such as $1.36 as opposed to 136.
"""

value = int(100 * float((input('enter the number of pennies that you have: ')))) #multiply by 100 to get to pennies

quarters = value // 25

value = value - (quarters * 25)

dimes = value // 10

value = value - (dimes * 10)

nickles = value // 5

value = value - (nickles * 5)

pennies = value

print('You have '+ str(quarters) + ' quarters, ' + str(dimes) + ' dimes' + ', ' + str(nickles) +' nickles' +', and ' + \
      str(pennies) + ' pennies.' )