class ATM:
    def __init__(self, balance = 0.00, interest_rate = .1):
        self.balance
        self.interest_rate


    def check_balance(self):
        return f'''Your account balance is {self.balance}'''

    def deposit(amount):
        self.balance += amount
    def check_withdrawal(amount):
        if amount <= self.balance:
            return f'''You may make a withdrawal'''
        else:
            return f'''You broke mutha fucka'''
        

    def withdraw(amount):
        self.balance -= amount

    def calc_interest(self):
        self.balance += self.balance * self.interest_rate

