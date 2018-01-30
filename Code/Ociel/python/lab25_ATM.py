# Class
# Version 1 to 3 is all included.

#################################################################
class ATM:
    def __init__(self, balances = 0, interests = 0.001):
        self.balance = balances
        self.interest = interests

    list_of_transactions = []

    def check_balance(self):
        print(f'Your balance is: ${self.balance}.')
    def deposit(self):
        deposit = float(input('How much would you like to deposit: '))
        self.balance += deposit
        self.list_of_transactions.append(f'User deposited ${deposit}' )
        return self.balance
    def check_withdrawal(self,amount):
        if self.balance - amount < 0:
            return False
        return True
    def withdraw(self):
        withdraw = float(input('How much do you want to withdraw: '))
        self.balance -= withdraw
        self.list_of_transactions.append(f'User withdrew ${withdraw}')
        return self.balance
    def calc_interest(self):
        return self.balance * self.interest
    def print_transactions(self):
        for i in self.list_of_transactions:
            print(i)



#######################################################################

checking = ATM()
user_info = 'not done'

while user_info != 'done':
    user_info = input('What would you ilike to do (deposit,'
                      'withdraw, check balance, history, or\n'
                      'done)? ').lower()

    if user_info == 'deposit':
        checking.deposit()
    elif user_info == 'withdraw':
        checking.withdraw()
    elif user_info == 'check balance':
        checking.check_balance()
    elif user_info == 'history':
        checking.print_transactions()


##########################################################################






