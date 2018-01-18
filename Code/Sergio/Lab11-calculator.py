while True:
    operator = input('What is the operation you\'d like to perform? +, -, *, / ? ')
    if operator == 'done':
        break

    num1 = int(input('What is the first number? '))
    num2 = int(input('What is the second number? '))

    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
    break
