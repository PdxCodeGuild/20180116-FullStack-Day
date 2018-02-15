change = int(input('How many pennies?\n:'))

change_dict = {'quarters': 25, 'dimes': 10, 'nickels': 5}

def make_change(change):
    if change is not change.keys():
        print('Please enter the amount.')
    elif change in change.keys():
        change % change_dict['quarters']
    