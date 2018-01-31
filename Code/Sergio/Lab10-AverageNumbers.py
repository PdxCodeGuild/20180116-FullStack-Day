"Version 1: Average numbers"
# nums = [5, 0, 8, 3, 4, 1, 6]
# numbersSum = sum(nums)
# numbersSum /= len(nums)
# print(numbersSum)


# Version 2
nums = []  # create empty list
user_choice = int(input('How many numbers would you like to average out? '))

for i in range(user_choice):  # loops based on user_choice
    number = int(input('Enter a number: '))  # prompt user for number
    nums.append(number)  # append to nums
print(nums)  # prints your list/numbers you want to average
numbersSum = sum(nums)
numbersSum /= len(nums)
print(f'Your average is: {numbersSum} ')
