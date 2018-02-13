# Problem 1: Write a function that tells whether a number is even or odd


def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


print(is_even(5))
print(is_even(6))
print('')

# Problem 2 Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.


def opposite(a, b):
    if a > 0 and b < 0:
        return True
    elif a < 0 and b > 0:
        return True
    else:
        return False

print(opposite(10, -1))
print(opposite(2, 3))
print(opposite(-1, -1))
print(opposite(-5, 3))
print('')

# Problem 3 Write a function that returns True if a number is within 10 of 100.

def near_100(num):
    if abs(100 - num) <= 10:
        return True
    else:
        return False

print(near_100(50))
print(near_100(99))
print(near_100(105))
print(near_100(90))
print(near_100(10))
print('')

# Problem 4 Write a function that returns the maximum of 3 parameters.


def maximum_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        print("Something's not right")

print(maximum_of_three(5,6,2))
print(maximum_of_three(-4,3,10))
print(maximum_of_three(76.9, 45, 78.90))
print(maximum_of_three('this','is a', 'string')) # why does this not go to the else?
print('')

# Problem 5 Print out the powers of 2 from 2^0 to 2^20


def powers_of_x(x):
    i = 0
    while i <= 20:
        print(x ** i)
        i += 1

powers_of_x(2)
