def factorial_iterative(n):
    r = n
    while n > 1:
        r = r * n
        n = n - 1
    return r

print(factorial_iterative(4))

#4*3*2*1


#two important parts: 1. Stop condition (if n = 1 return 1). 2. recursive call.


def factorial_recursive(n):
    if n == 1: #stop condition
        print('returning 1')
        return 1
    return n*factorial_iterative(n-1) #recursive call


def factorial_recursive(n, depth):
    print('\t' * depth + f'factorial({n})')
    if n == 1: #stop condition
        print('\t' *depth + 'returning 1')
        return 1
    print('\t' * depth + f'calling factorial{n - 1}')
    return n*factorial_iterative(n-1) #recursive call

factorial_iterative(10, 0)

def infinite_recursion(): #Infinite recursion.
    infinite_recursion()

def infinite_recursion(): #Infinite recursion. Maximum number with this one that was called up was 1000 in class.
    global number_of_calls
    print(number_of_calls)
    infinite_recursion()

def infinite_loop():  #infinite loop
    while True:
        pass


#fibonachi sequence

def fibonacci_iterative(n): #Sum of last two numbers?
    num_1 = 0
    num_2 = 1
    for i in range(n):
        fn = num_1 + num_2
        #Not finished

def fibonacci_recurssive(n):
    if n == 0 or n == 1:
        return 1
    return factorial_recursive(n-1) + fibonacci_recurssive(n-2)

# base case is what the stop is called.
