"""
Lab 8
Let's make some change!
"""

money = input("How much money do you have?\n: ")
total = float(money) * 100

quarters = int(total) // 25
dimes = (int(total) - quarters * 25) // 10
nickles = ((int(total) - quarters * 25) - dimes * 10) // 5
pennies = ((int(total) - quarters * 25) - (dimes * 10) - nickles * 5) // 1

print("\nYou can convert that to " + str(quarters) + " quarters, " + str(dimes) + " dimes, " + str(nickles) + " nickles, and " + str(pennies) + " pennies!")
