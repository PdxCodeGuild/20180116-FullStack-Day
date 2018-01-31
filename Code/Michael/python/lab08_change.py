def change(x):

    amount = float(x)

    quarters = amount // 25
    qremainder = amount % 25

    dimes = qremainder // 10
    dremainder = qremainder % 10

    nickles = dremainder // 5
    nremainder = dremainder % 5

    pennies = nremainder // 1

    print(f'You have {quarters} quarters, {dimes} dimes, {nickles} nickles and {pennies} pennies.')

change(166)