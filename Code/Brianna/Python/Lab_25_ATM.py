from datetime import datetime
current_time = datetime.now()

print("Welcome to the ATM of heroes!")

class ATM:
    """Giving our ATM class ATM-like functionality"""

    def __init__(self, account_holder, balance=0.00):  # Not really sure what should go here, if anything.
        self.balance = balance
        self.account_holder = account_holder
        self.print_transactions = []

    def balance(self, deposit):
        self.balance += deposit
        return self.balance

    def check_card(self, card_number):
        def get_second_digit(num):  # Using version of credit card check provided by Matthew in Solutions.
            if num < 10:
                return None
            # num_str = str(num)
            # return int(num_str[1])
            return num % 10

        def validate_credit_card(cc_str):
            if len(cc_str) != 16:
                return False
            # convert the string into a list of ints
            cc = []
            for i in range(len(cc_str)):
                cc.append(int(cc_str[i]))

            check_digit = cc.pop(-1)  # step 1
            cc.reverse()  # step 2
            for i in range(0, len(cc), 2):
                cc[i] *= 2  # step 3
            total = 0
            for i in range(len(cc)):
                if cc[i] > 9:
                    cc[i] -= 9  # step 4
                total += cc[i]  # step 5
            second_digit = get_second_digit(total)  # step 6
            return second_digit == check_digit

        credit_card_str = card_number
        print(validate_credit_card(credit_card_str))

    @staticmethod
    def interest():
        enter_interest = input("Would you like to enter in a new interest rate? y or n?")
        if enter_interest = 'y':
            rate = input("What is the interest rate?\n:")
        else:
            rate = 0.1
        return rate

    def account_holder(self, username):
        pass


    def account(self, account_holder, balance): # account holder name, sub accounts,
        pass

    def calculate_interest(self, balance, rate):
        new_balance = balance + (balance * rate)
        return new_balance

    def print_transactions(self, balance, transaction_amount):
        self.balance += transaction_amount
        print(f'This is your transaction amount {transaction_amount}.)
        print(f'This is your new balance {balance}')

