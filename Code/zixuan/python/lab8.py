
amount = float(input("please enter your amount of dollar "))
amount = amount * 100

Quater = int(amount / 25)
amount = amount - Quater * 25

Dime = int(amount / 10)
amount = amount - Dime * 10

Nickel = int(amount / 5)
Penny = amount - 5 * Nickel

Quater = str(Quater)
Dime = str(Dime)

Nickel = str(Nickel)
Penny = str(Penny)

print("it is equal to " + Quater + " quater " + Dime + " Dimes " + Nickel + " Nickels and " + Penny + " Pennies")
