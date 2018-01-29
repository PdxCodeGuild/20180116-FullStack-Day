"""
Optional lab
Arbitrary Precision Arithmetic
"""

from mpmath import *

mp.dps = 100
print(mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2)

print("Give me two ridiculously long numbers: ")
num1 = input("Number 1: ")
num2 = input("Number 2: ")

# Addition

result = int(num1) + int(num2)

num1_list = list(num1)
num2_list = list(num2)

print(num1_list)
print(num2_list)


print(f"{num1} + {num2} = {result}")


# Multiplication