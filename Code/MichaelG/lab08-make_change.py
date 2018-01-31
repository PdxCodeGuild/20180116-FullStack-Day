v = input('Please enter how much you have in pennies')
v = int(v)
q = v // 25
v -= q*25
d = v//10
v -= d*10
n = v//5
v -= n*5

print('You have ' + str(q) + ' quarters, ' + str(d) + ' Dimes, ' + str(n) + ' Nickels')
print(f'You have {q} quarters, {d} Dimes, {n} Nickels, and {v} Pennies')
