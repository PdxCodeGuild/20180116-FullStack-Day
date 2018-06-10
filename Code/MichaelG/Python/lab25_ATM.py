import random


class Atm():

    def __init__(self, name, balance = 0.0, rate = .001):
        self.name = name
        self.balance = balance
        self.rate = rate
        self.history = []

    def change_name(self):
        old_name = self.name
        self.name = input('Enter the new name')
        print(f'Changed account name from {old_name} to {self.name}')
        self.history.append(f'Changed account name from {old_name} to {self.name}')

    def check_balance(self):
        print('Balance: ', self.balance)
        self.history.append('Checked balance.')

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited ' + '${:,.2f}'.format(amount))
        self.history.append(f'Deposited ' + '${:,.2f}'.format(amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have that much in your account")
        else:
            self.balance -= amount
            print(f'Withdrew ' + '${:,.2f}'.format(amount))
            self.history.append(f'Withdrew ' + '${:,.2f}'.format(amount))

    def calc_interest(self):
        self.balance = self.balance * (1 + self.rate)
        print('Applied interest')
        self.history.append('Applied interest')

    def show_history(self):
        print('Account History:')
        for item in self.history:
            print('\t', item)

def get_amount(string):
    return float(input('How much would you like to ' + string + '? '))


accounts = list()
names = ['Michael', 'Wes', 'Anna', 'Brianna', 'Maggie']
balances = [30.34, 1234.00, 45.01, 67.23, 89.34, 998.45]
rates = [.001, .002, .003, .004, .005]
accounts = [Atm(random.choice(names), random.choice(balances), random.choice(rates)) for i in range(5)]


print('Here are the randomly generated accounts:')
for i in range(5):
    print(str(i+1) + ') Name: ', accounts[i].name.ljust(12), 'Balance:', '${:,.2f}'.format(accounts[i].balance).ljust(12),
          'Interest rate: ', accounts[i].rate)


while True:
    # User chooses which account to work with
    account_number = int(input('Which account do you want to access, (0 to quit)? '))

    if account_number == 0:
        break


    account_index = account_number - 1

    stay = True
    while True:
        print(str(account_number) + ') Name: ', accounts[account_index].name.ljust(12), 'Balance:',
              '${:,.2f}'.format(accounts[account_index].balance).ljust(12),
              'Interest rate: ', accounts[account_index].rate)
        print('What would you like to do? ')
        print('1) change account name  2) deposit  3) withdraw  '
           '4) check balance  5) apply interest  6) show history  7) change accounts')
        choice = int(input('?'))
        if choice == 1:
            accounts[account_index].change_name()
        elif choice == 2:
            accounts[account_index].deposit(get_amount('deposit'))
        elif choice == 3:
            accounts[account_index].withdraw(get_amount('withdraw'))
        elif choice == 4:
            accounts[account_index].check_balance()
        elif choice == 5:
            accounts[account_index].calc_interest()
        elif choice == 6:
            accounts[account_index].show_history()
        else:
            break

        print('*' * 50)


