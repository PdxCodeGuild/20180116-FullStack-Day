# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

a = int(input('Number please\n:'))


def even_odd(a):
    return a % 2


if even_odd(a) == 0:
    print('Even')
elif even_odd(a) != 0:
    print('odd')

# Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

b = int(input('First number'))
c = int(input('Second number\n:'))


def pos_neg(b, c):
    if b > 0 and c < 0 or b < 0 and c > 0:
        return True
    else:
        return False


# Write a function that returns True if a number within 10 of 100.

d = int(input('Number\n:'))


def fun_ction(d):
    if d >= 10 and d <= 100:
        return True
    else:
        return False


# Write a function that returns the maximum of 3 parameters.

e = int(input('First num\n:'))
f = int(input('Second num\n:'))
g = int(input('Third num\n:'))


def fun_max(e, f, g):
    return max(e, f, g)



#Print out the powers of 2 from 2^0 to 2^20
def power_to(a):
    for a in range(20):
        print(a ** 2)

power_to(2)