valid_ops = ['+', '-', '*', '/', 'd']

def get_op():
    while True:
        op = input('Enter the operation: ')
        if op in valid_ops:
            return op


def get_num(n):
    request = 'Enter number ' + str(n) + ': '
    while True:
        num = input(request)
        try:
            num = float(num)
            break
        except ValueError:
            print('Enter a number please')
    return num


while True:
    operation = get_op()
    if operation == 'd':
        break
    else:
        num1 = str(get_num(1))
        num2 = str(get_num(2))

        expression = num1 + operation + num2

    try:
        x = eval (expression)
        print (expression, '=', x)
    except ZeroDivisionError:
        print('You tried to divide by zero, start over...')
