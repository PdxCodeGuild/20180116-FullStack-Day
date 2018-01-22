

while True:
    sign = input('What is the operation you would like to perform? Or enter done ')
    if sign == 'done':
        print('Goodbye.')
        break
    fn = input('What is the first number? ')
    sn = input('What is the second number? ')

    t = int(fn)
    u = int(sn)

    q = t + u
    v = t - u
    x = t * u
    z = t / u
    if sign == '+':
        print(q)

    elif sign == '-':
        print(v)

    elif sign == '*':
        print(x)

    elif sign == '/':
        print(z)








