# Version 1 and 2 combined


calculate = 0

while True:
    operation = input('What is the operation you"d like to perform? ')
    if operation == 'done':
        break
    firstNumber = input('What is the first number? ')
    secondNumber = input("What is the second number? ")
    if operation == '*':
        calculate = int(firstNumber) * int(secondNumber)
    if operation == '+':
        calculate = int(firstNumber) + int(secondNumber)
    if operation == '/':
        calculate = int(firstNumber) / int(secondNumber)
    if operation == '-':
        calculate = int(firstNumber) - int(secondNumber)
    print(f'{firstNumber} {operation} {secondNumber} = {calculate}')



# Version 3
