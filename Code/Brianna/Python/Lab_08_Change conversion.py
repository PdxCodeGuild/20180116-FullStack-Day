#Defining the value of money in number of pennies
quarters = 25
dimes = 10
nickles = 5
pennies = 1

#Define what the user needs to input
amount = float(input("Please enter an amount of money in pennies. For example, for $2.56 enter 256.\n:"))

#Do the math
# Quarters
number_of_quarters = amount // quarters
remainder = amount % 25

# Dimes

number_of_dimes = remainder // dimes
remainder = remainder % 10

# Nickles
number_of_nickles = remainder // nickles
remainder = remainder % 5

# Pennies
number_of_pennies = remainder


#Output
print("You have " + str(number_of_quarters) + " quarters, " + str(number_of_dimes) + " dimes, " + str(number_of_nickles) + " nickles, and " + str(number_of_pennies) + " pennies.")

