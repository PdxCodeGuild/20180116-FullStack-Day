"""
Lab 25 - ATM
"""


# ATM class with all functions
class ATM:
    def __init__(self, balance, interest=0.1):
        self.balance = balance
        self.interest = interest
        self.transactions = []

    def check_balance(self):  # checks balance
        return f"Your balance is: ${self.balance}"

    def deposit(self, amount):  # deposits to balance
        self.balance += amount
        print(f"Deposit amount: {amount}")
        return self.balance

    def check_withdrawal(self, amount):  # checks balance to see if we can withdraw
        if self.balance - amount > 0:
            return True
        else:
            print('Not enough funds to withdraw.')

    def withdraw(self, amount):  # deposits to balance
        self.balance -= amount
        print(f"You have withdrawn: {amount}")
        return self.balance

    def calc_interest(self):
        self.balance += self.balance * self.interest
        print(f"Interest: {self.interest}%")
        return self.balance

    def print_transactions(self):
        return "Transaction history:\n\t" + '\n\t'.join(self.transactions)


# testing
checking_account = ATM(50000)
print(checking_account.check_balance())
print(checking_account.check_withdrawal(900))
print(checking_account.withdraw(900))
print(checking_account.check_balance())
print(checking_account.deposit(int(1000)))
print(checking_account.check_balance())
print(checking_account.withdraw(1500))  # change to ridiculously high number to get else statement
print(checking_account.deposit(2500))
print(checking_account.calc_interest())
