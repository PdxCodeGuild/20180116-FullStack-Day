def check_balance(account):
    print(f'Balance: {account}')
    return account


def deposit(account):
    amount = input("How much money would you like to deposit?\n> ")
    account += int(amount)
    history.append(f'user deposited ${amount}')
    print(account)
    return account


def check_withdrawal(account):
    amount = input('How much money would you like to withdraw from your account?\n> ')
    while int(amount) > account:
        amount = input(f'Not enough money in account, please enter an amount less than or equal to {account}.\n> ')
    return amount


def withdrawal(account):
    amount = check_withdrawal(account)
    account = account - int(amount)
    history.append(f'user withdrew ${amount}')
    print(f'New balance: {account}')
    return account


def calc_interest(account):
    interest = account * 0.1
    print(f'Interest earned on an account worth ${account}: ${interest}')
    return interest


def print_history():
    print(history)
    return history

def start(account):
    choice = input('What would you like to do? (deposit, withdrawal, check balance, history, interest, done)\n> ').lower()
    if choice == 'deposit':
        account = deposit(account)
    elif choice == 'withdrawal':
        account = withdrawal(account)
    elif choice == 'check balance':
        account = check_balance(account)
    elif choice == 'interest':
        account == calc_interest(account)
    elif choice == 'history':
        print_history()
    elif choice == done:
        exit()
    start(account)


history = []
balance = 100
start(balance)