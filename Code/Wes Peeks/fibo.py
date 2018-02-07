def fib_rec(num1, num2, iterations):
    num3 = num1 + num2
    print(num3)
    iterations -= 1
    if iterations == 0:
        return 0
    else:
        fib_iter(num2, num3, iterations)


def fib_recu(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib_recu(x - 2) + fib_recu(x - 1)


num1 = 0
num2 = 1
num3 = 0
print(num1, num2)
while num3 < 100:
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3

# print(fib_recu(6))