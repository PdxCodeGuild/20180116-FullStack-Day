# Start with empty list for user to fill
nums = []

# User input for first number of list
num = input('Please enter the first number of your list you wish to average: ')

# User input for res of numbers to be averaged
while num != 'done':
    nums.append(int(num))
    num = input('Input next number in your list or \'done\'. ')

# Start our count for our sum at 0
sum = 0

# Add each number in our list together using a running sum
for i in range(len(nums)):
    sum += nums[i]
    i += 1

# Average the numbers in the list using found sum.
average = sum / len(nums)

print(f'The average of the numbers is {average}.')