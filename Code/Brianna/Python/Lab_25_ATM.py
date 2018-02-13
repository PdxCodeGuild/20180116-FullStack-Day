from datetime import datetime
current_time = datetime.now()

print("Welcome to the ATM of heroes!")

try_atm = ATM(account_holder())
selection = user_input()


class ATM:
    """Giving our ATM class ATM-like functionality"""

    def __init__(self, account_holder, balance=0.00):  # Not really sure what should go here, if anything.
        self.balance = balance
        self.account_holder = account_holder
        self.print_transactions = []

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.print_transactions.append(f"You deposited {deposit_amount}. Thank you {self.account_holder}! "
                                       f"{now.strftime('%Y-%m-%d at %H:%M')}")
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
    """Set an interest rate or go to the default of 0.01"""
    def interest(self):
        enter_interest = input("Would you like to enter in a new interest rate? y or n?")
        if enter_interest == 'y':
            self.rate = input("What is the interest rate?\n:")
        else:
            self.rate = 0.1
        return self.rate

    """ Let users tell the ATM who they are for access to their account"""
    def account_holder(self, username):
        username = input("What is your name?")
        self.username = username
        self.account_holder = self.username
        return self.account_holder

    # Possibly use this to create multiple accounts/account types?
    def account(self, account_holder, account_type, balance): # account holder name, sub accounts,
        pass

    """Calculate the interest on an account."""
    def calculate_interest(self):
        new_balance = self.balance + (self.balance * self.rate)
        return new_balance

    def print_transactions(self, balance, transaction_amount):
        self.balance += transaction_amount
        print(f'This is your transaction amount {transaction_amount}.')
        print(f'This is your new balance {balance}')

    def user_selections(self):
        print("You have entered the world of ATM. Your life now revolves around validate card, deposit, withdraw, check balance, calculate interest, and check history.")
        print("""\
                       *     .--.
                            / /  `
           +               | |
                  '         \ \__,
              *          +   '--'  *
                  +   /\
     +              .'  '.   *
            *      /======\      +
                  ;:.  _   ;
                  |:. (_)  |
                  |:.  _   |
        +         |:. (_)  |          *
                  ;:.      ;
                .' \:.    / `.
               / .-'':._.'`-. \
               |/    /||\    \|
         jgs _..--\"""````"""""""--.._
       _.-'``                    ``'-._
     -'                                '-""")
        print("What would you like to do?")
        user_input = input("...")
        return user_input


# Make a subclass???  Maybe for other types of accounts?
# example class ATM_Savings(ATM):

def use_atm(choice):
    if choice == 'deposit':
        print("How much money are you feeding the alie...ATM... today?")
        amount = float(input("..."))
        print(try_atm.deposit(amount))
        again = input("Would you like to feed me...deposit more money? y/n ")
        if again == 'y':
            choice = user_input()
            try_atm(choice)
        else:
            print("Goodbye!")
    elif choice == 'withdraw':
        print("How much would you like to withdraw?")
        amount = float(input("> "))
        print(my_atm.withdraw(amount))
        again = input("Would you like to complete another transaction? y/n ")
        if again == 'y':
            choice = user_input()
            use_atm(choice)
        else:
            print("Goodbye!")
    elif choice == 'check balance':
        print(my_atm.check_balance())
        again = input("Would you like to complete another transaction? y/n ")
        if again == 'y':
            choice = user_input()
            use_atm(choice)
        else:
            print("Goodbye!")
    elif choice == 'check history':
        print(my_atm.print_transactions())
        again = input("Would you like to complete another transaction? y/n ")
        if again == 'y':
            choice = user_input()
            use_atm(choice)
        else:
            print("Goodbye!")
    else:
        print("That is not a valid option.")
        again = input("Would you like to complete another transaction? y/n ")
        if again == 'y':
            choice = user_input()
            use_atm(choice)
        else:
            print("Goodbye!")

