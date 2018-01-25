# no imports

#variables
valid = True

# ask the user for a credit card number and convert to an int
cc = input('Please enter the credit card number (separated by spaces): ')

# Convert the input string into a list of ints
list = [int(x) for x in cc.split(' ')]
lastnumbercc = list[-1]
print(lastnumbercc)
print(list)

# Slice off the last digit. That is the check digit.
list = list[:len(list)-1]
print(list)

# Reverse the digits.
list = list[::-1]
print(list)

# Double every other element in the reversed list.
for i in range(0, len(list), 2):
    list[i] *= 2
print(list)

# Subtract nine from numbers over nine.
for i in range(0, len(list)):
    if list[i] > 9:
        list[i] -= 9
print(list)

#sum1 = sum(list) #easier way
sum = 0
# Sum all values.
for i in range(0, len(list)):
    sum += list[i]
print(sum)

# Take the second digit of that sum.
lastdigit = sum % 10
print(lastdigit)

# If that matches the check digit, the whole card number is valid.
if lastdigit == lastnumbercc:
    print(valid)
else:
    valid = False
    print(valid)