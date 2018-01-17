# User input for operation
oper = input('Which operation would you like to perform? ')

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

print(f'{num1} {oper} {num2} = {output}')