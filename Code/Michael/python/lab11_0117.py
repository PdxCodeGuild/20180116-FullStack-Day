print('''
Select operator.
Addition
Subtracting
Multiplication
Division
''')

operator = input('What is the operation you\'d like to perform?\n> ')

first = int(input('> What is the first number?\n> '))
second = int(input('> What is the second number?\n> '))

if operator == '+':
    print(first,"+",second,"=", first + second)

elif operator == '-':
    print(first,"-",second,"=", first - second)

elif operator == '*':
    print(first,"*",second,"=", first * second)

elif operator == '/':
    print(first,"/",second,"=", first / second)

else:
    print('Something isn\'t correct!')