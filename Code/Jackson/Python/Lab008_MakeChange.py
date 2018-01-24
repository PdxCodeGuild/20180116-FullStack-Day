"""
Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the
number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in
the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder.
10/3 is 3.333333, 10//3 is 3.
"""

value = int(input('enter the number of pennies that you have: '))

quarters = value // 25

value = value - (quarters * 25)

dimes = value // 10

value = value - (dimes * 10)

nickles = value // 5

value = value - (nickles * 5)

pennies = value

print('You have '+ str(quarters) + ' quarters, ' + str(dimes) + ' dimes' + ', ' + str(nickles) +' nickles' +', and ' + \
      str(pennies) + ' pennies.' )