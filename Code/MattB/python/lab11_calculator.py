while True:

    # User input for operation
    oper = input('Which operation would you like to perform? ')
    if oper == 'done':
        break
    else:
        # User input for numbers
        num1 = int(input('What is your first number? '))
        num2 = int(input('What is your second number? '))

    # Operations
    if oper == '+':
        output = num1 + num2
    elif oper == '-':
        output = num1 - num2
    elif oper == '*':
        output = num1 * num2
    elif oper == '/':
        output = num1 / num2
    elif oper == 'done':
        break

    # Print full operation
    print(f'{num1} {oper} {num2} = {output}')



