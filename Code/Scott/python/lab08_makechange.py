


# define input as amount_penny
# make input the total amount of pennies
# convert input into integer
# define quarters as amount_penny//25

unconverted_pennies = int(input('Enter the dollar amount in pennies (ie. $1.36 would be 136.): '))
quarters = unconverted_pennies//25
dimes = unconverted_pennies%25//10
pennies = unconverted_pennies%10
print(str(quarters) + ' quarters, ' + str(dimes) + ' dimes, and ' + str(pennies) + ' pennies')

