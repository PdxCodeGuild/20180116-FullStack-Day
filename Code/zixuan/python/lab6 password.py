import string
import random
s1=''
s2=''
char=string.ascii_letters
n=int(input("input the length of the string:"))
j=0
while j<n:
    s2 += random.choice(char)
    j=j+1


for i in range(n):
    s1 += (random.choice(char))

print(s2)