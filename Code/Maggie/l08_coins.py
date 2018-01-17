'Making change'


def start():
    ch = input('Choose either A or B:\n(a.) Convert a number of pennies to a dollar amount?\n'
          'or\n(b.) convert a dollar amount to a number of pennies?\nYour Choice: ').upper()
    if ch == 'A':
        p_to_d()
    elif ch == 'B':
        d_to_p()
    else:
        print('Please make a valid entry')
        start()

# input number of pennies
def p_to_d():
    pennies = input('Enter the number of pennies (ie, 167).\nPennies: ')
    print('You have ', int(pennies)//100, ' dollars and ', int(pennies) % 100, ' cents.')


def d_to_p():
    dollars = input('Enter the number of dollars and cents (ie, 1.67).\nDollars and cents: ')
    print('You have ', round(float(dollars) * 100), 'pennies')


# ask if user would like to convert # of pennies to dollars or dollars to pennies
print('Dollars and Pennies\n')
start()