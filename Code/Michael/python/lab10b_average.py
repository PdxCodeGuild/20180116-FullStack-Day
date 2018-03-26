# Lab 10: Average Numbers
# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.
#
# The code below hows how to loop through an array, and prints the elements one at a time.
#
# nums = [5, 0, 8, 3, 4, 1, 6]
#
# # loop over the elements
# for num in nums:
#     print(num)
#
# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])
# Version 2
# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.
#
# Lab 10: Average Numbers
# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.
#
# The code below hows how to loop through an array, and prints the elements one at a time.



nums = []
i = 0

while True:

    nums = int(input('Enter a number to be averaged.\n> '))

    while i in nums:
        nums.append(i)

        if user enters a number
            nums.append to nums
        elif:
            sumnumber /= len(nums)

print(sumnumber)










# nums = []
# i = 0
#
# for i in nums:
#     nums.append(int(input('Enter a number to be averaged.\n> ')))
#
# while i in nums:
#     nums.append()
#     i += 1
#
#     if user enters a number
#         append to nums
#     elif user enters done
#         average the numbers by length of sum
#
# sumnumber = sum(nums)
# sumnumber /= len(nums)
#
# print(sumnumber)
#
