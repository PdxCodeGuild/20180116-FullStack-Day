def add(first, second):
    return first + second

def subt(first, second):
    return first - second

def mult(first, second):
    return first * second

def divi(first, second):
    return first / second

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
    print(first,"+",second,"=", add(first,second))

elif operator == '2':
    print(first,"-",second,"=", subt(first,second))

elif operator == '3':
    print(first,"*",second,"=", mult(first,second))

elif operator == '4':
    print(first,"/",second,"=", divi(first,second))

else:
    print('Enter a damn number!')