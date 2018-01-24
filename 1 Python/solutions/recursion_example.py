
def factorial_iterative(n):
    r = 1
    while n > 1:
        r *= n
        n -= 1
    return r

print(factorial_iterative(4))

def factorial_recursive_print(n, depth):
    print('\t'*depth + f'factorial({n})')
    if n == 1:
        print('\t'*depth + 'returning 1')
        return 1
    print('\t' * depth + f'returning {n}*factorial {n-1}')
    return n*factorial_recursive_print(n-1, depth+1)


def factorial_recursive(n):
    if n == 1:
        return 1
    return n*factorial_recursive(n-1)


#factorial_recursive(10, 0)


def infinite_loop():
    while True:
        pass


number_of_calls = 0
def infinite_recursion():
    global number_of_calls
    number_of_calls += 1
    print(number_of_calls)
    infinite_recursion()
#infinite_recursion()



def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return 1
    return factorial_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(5))











