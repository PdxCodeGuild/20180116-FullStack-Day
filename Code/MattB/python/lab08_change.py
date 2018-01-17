print('Let\'s find out how much change you can make.')

money = float(input('Please input a dollar amount with a decimal: '))

nmoney = int(money * 100)

quarters = nmoney // 25

qmoney = nmoney % 25

dimes = qmoney // 10

dmoney = qmoney % 10

nickels = dmoney // 5

pennies = dmoney % 5

print(f'From your {money} you\'ll have {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.')