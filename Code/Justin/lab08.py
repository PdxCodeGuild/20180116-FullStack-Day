def get_amount():
    a = ('How much? ')
    while True:
        a = input('How much? ')
        try:
            float(a)
            break
        except ValueError:
            print('Enter a number, please.')
    v = float (a)
    v = v * 100
    v = round(v)
    return v

def divide(v, c):
    n = v // c
    r = v % c
    return (n, r)


while True:
    amount = get_amount()
    coins = ['quarters', 'dimes', 'nickles', 'pennies']
    amounts = [25, 10, 5, 1]

    print ('Your amount in change is...')
    for i in range(4):
        number, remainder = divide (amount, amounts[i])
        print('this many ',coins[i], ': ', number)
        amount = remainder
    again = input ('Wanna do this again? Enter \'n\' to quit.')
    if again == 'n':
        break





