print('''
Select operator.
1. Addition
2. Subtracting
3. Multiplication
4. Division
''')

operator = input('What is the operation you\'d like to perform?\n> ')

first = int(input('> What is the first number?\n> '))
second = int(input('> What is the second number?\n> '))

if operator == '1':
    print(first,"+",second,"=", first + second)

elif operator == '2':
    print(first,"-",second,"=", first - second)

elif operator == '3':
    print(first,"*",second,"=", first * second)

elif operator == '4':
    print(first,"/",second,"=", first / second)

else:
    print('Enter a damn number!')