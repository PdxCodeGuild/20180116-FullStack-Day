# List of numbers we want to average
nums = [5, 0, 8, 3, 4, 1, 6]

# Start our count for our sum at 0
sum = 0

for i in range(len(nums)):
    sum += nums[i]
    i += 1

# Average the numbers in the list using found sum.
average = sum / len(nums)

print(f'The average of the numbers is {average}.')