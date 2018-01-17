"""
Lab 8
Let's make some change!
"""

money = input("How much money do you have?\n: ")
total = int(float(money) * 100)

quarters = total // 25
total -= quarters * 25
dimes = total // 10
total -= dimes * 10
nickles = total // 5
total -= nickles * 5
pennies = total // 1

print(f"\nYou can convert that to {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies!")
