
import random
import string

letters = string.ascii_letters + string.digits + string.punctuation
print(letters)

nums = [random.randint(0, 99) for i in range(100)]
nums = [num for num in nums if num%2 == 0]
print(nums)

passwords = [''.join([random.choice(letters) for i in range(20)]) for j in range(10)]
password = ''.join([random.choice(letters) for i in range(20)])
print(passwords)

matrix_size = 4
identity = [[1 if i == j else 0 for j in range(matrix_size)] for i in range(matrix_size)]
for row in identity:
    print(row)

names = ['jane', 'joe', 'bob']
ages = [29, 23, 12]
peeps = {names[i]:ages[i] for i in range(len(names))}
print(peeps)

passwords = [''.join([random.choice(letters) for i in range(int(input('how long should the password be? ')))]) for j in range(int(input('how many passwords would you like? ')))]

print(passwords)

