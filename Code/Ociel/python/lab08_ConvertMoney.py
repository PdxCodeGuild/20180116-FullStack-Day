
amount = float(input("Please enter amount of pennies: "))

quarter = 0
dime = 0
nickles = 0

if amount >= 25:
    quarter = amount // 25
    amount = amount - (quarter * 25)
if amount >= 10:
    dime = amount // 10
    amount = amount - (dime * 10)
if amount >= 5:
    nickles = amount // 5
    amount = amount - (nickles * 5)

print(f"You have {int(quarter)} quarters.\n"
      f"You have {int(dime)} dimes.\n"
      f"You have {int(nickles)} nickles.\n"
      f"YOu have {int(amount)} pennies.")


# # Version 1
# userAnswer = int(input("Please provide an amount of pennies: "))
#
# cents = userAnswer % 100
#
# if userAnswer >= 100:
#     dollar = userAnswer // 100
#     print(f"Your total amount is ${dollar}.{cents}")
# else:
#     print(f"Your total amount is .{cents}")
#
#
#



# # Version 2
#
# userAnswer2 = float(input("Please provide a dollar amount. (Ex. 1.36): "))
# answer = userAnswer2 * 100.00
# print("You have " + str(int(answer)) + " pennies!")
