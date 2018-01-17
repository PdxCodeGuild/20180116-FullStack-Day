"Version 1: Average numbers"
# nums = [5, 0, 8, 3, 4, 1, 6]
# numbersSum = sum(nums)
# numbersSum /= len(nums)
# print(numbersSum)


#Version 2
nums = []  # create empty list

for i in range(0, 7):  # set up loop to run 7 times
    number = int(input('Enter a number: '))  # prompt user for number
    nums.append(number)  # append to nums
print(nums)
numbersSum = sum(nums)
numbersSum /= len(nums)
print('Your average is: ')
print(numbersSum)


# # loop over the elements
# for num in nums:
#     print(num)
#
# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])
