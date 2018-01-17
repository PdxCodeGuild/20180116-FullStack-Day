#Defining the value of money in number of pennies
quarters = .25
dimes = .10
nickles = .5
pennies = .1

#Define what the user needs to input
amount = float(input("Please enter an amount of money in pennies. For example, for $2.56 enter 2.56.\n:"))

#Do the math
number_of_quarters = amount // quarters
number_of_dimes = (amount - (number_of_quarters * quarters)) // dimes
number_of_nickles = (amount - (number_of_dimes + (number_of_dimes * dimes))) // nickles
number_of_pennies = (amount - (number_of_nickles + (number_of_nickles * nickles))) // pennies

#Output
print("You have " + str(number_of_quarters) + " quarters, " + str(number_of_dimes) + " dimes, " + str(number_of_nickles) + " nickles, and " + str(number_of_pennies) + " pennies.")
