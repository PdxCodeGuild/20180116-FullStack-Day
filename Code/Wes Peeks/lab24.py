toDO = input('What would you like to do?')
my_atm = ATM()


class ATM:

    def __init__(self):
        self.balance = 0
        self.interest = 0.001
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append('user deposited $' + amount)

    def check_withdrawal(self, amount):
        a = self.balance - amount
        if a < 0:
            return False
        else:
            return True

    def withdrawal(self, amount):
        self.balance = self.balance - amount
        self.transactions.append('user withdrew $ ' + amount)

    def calc_interest(self):
        return self.balance * self.interest



this_atm = ATM()

print(this_atm.check_balance())



