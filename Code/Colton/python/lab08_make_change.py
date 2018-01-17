print("Let's make some change")
#establishing varibales
quarter = 25
dime =  10
nickel = 5
penny = 1
money = input("How many pennies do you have?\n:")
money = int(money)#convertong string to integer
# simpler way to do this math? I tend to overcomplicate things
change_q = money // quarter
money1 = change_q * quarter
money = money - money1
change_d = money // dime
money2 = change_d * dime
money = money - money2
change_n = money // nickel
money3 = change_n * nickel
money = money - money3
change_p = money // penny

#converting integers to strings
change_q = str(change_q)
change_d = str(change_d)
change_n = str(change_n)
change_p = str(change_p)

print(f"""You can have {change_q} qaurters, {change_d} dimes, {change_n} nickels, and {change_p} pennies.""")


