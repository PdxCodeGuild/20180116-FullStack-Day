import string
import random

c1 = string.ascii_lowercase
c2 = string.ascii_uppercase
s1 = []
s2 = []

A = int(input("input amount of higher case:"))
a = int(input("input amount of lower case:"))
j = 0
while j < a:
    s1.append(random.choice(c1))
    j = j + 1

for i in range(A):
    s1.append(random.choice(c2))

s2 = random.sample(range(a + A), a + A)

code = ""
for i in range(a + A):
    code = code + s1[s2[i]]

print(code)
