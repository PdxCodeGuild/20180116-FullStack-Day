# Lab 10: Average Numbers
# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.
#
# The code below hows how to loop through an array, and prints the elements one at a time.




nums = [5,0,8,3,4,1,6]
i = 0

while i in nums:
    nums.append(2)
    i += 1

sumnumber = sum(nums)
sumnumber /= len(nums)

print(sumnumber)



# nums = [5,0,8,3,4,1,6]
#
# for i in nums:
#     nums.append(int(input('Enter a number to be averaged.\n> ')))
#
# sumnumber = sum(nums)
# sumnumber /= len(nums)
#
# print(sumnumber)
