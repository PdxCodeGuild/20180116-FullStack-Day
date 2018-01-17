amount = float(133.00)

if amount >= 100:
    dollars = amount // 100
    change = amount % 100
    print(f'{dollars} {change}')
else:
    print(amount)

quarters = amount // 25
qremainder = amount % 25
dimes = qremainder // 10
dremainder = dimes % 10
nickles = dremainder // 5
nremainder = nickles % 5
pennies = nremainder // 1

print(f'you have {quarters} quarters, {dimes} dimes, {nickles} nickles and {pennies}')