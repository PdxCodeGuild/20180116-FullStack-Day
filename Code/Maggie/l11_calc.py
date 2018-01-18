'''CALCULATOR

A simple python calculator that can perform addition, subtraction, multiplication and division.
'''

def main():
    print('A Python Calculator!\n')
    print('What type of operation would you like to perform?\n(You can enter: +, -, *, / or "done" to quit.)')
    operator = input('Your entry: ')
    first = input('What is the first number? ')
    second = input('What is the second number? ')

    if operator == '+':
        print(str(first) + ' + ' + str(second) + '=', float(first) + float(second))
    elif operator == '-':
        print(str(first) + ' - ' + str(second) + '=', float(first) - float(second))
    elif operator == '*':
        print(str(first) + ' * ' + str(second) + '=', float(first) * float(second))
    elif operator == '/':
        print(str(first) + ' / ' + str(second) + '=', float(first) / float(second))
    elif operator == 'done':*
        quit()
    else:
        print("invalid operation.")
        tryagain()
    tryagain()

def tryagain():
    retry = input('Would you like to try again? (y/n): ')
    if retry.upper() == 'Y':
        main()
    else:
        quit()
def quit():
    print('\nBe seeing you!')

main()


