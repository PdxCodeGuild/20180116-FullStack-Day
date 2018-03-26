# nums = []
#
# user_num = input('What number would you like to add?\n:')
# user_num = num.append()
#
# for num in nums:
#     print(num)
#
# for i in range(len(nums)):
#     print(nums[i])

nums = []
user_num = input('What number would you like to add?\n:')
nums.append(user_num)
while user_num != 'fini':
    user_num = input('What number would you like to add? To exit type fini.\n:')
    nums.append(user_num)
    if user_num == 'fini':
        nums.pop()


nums = [int(i) for i in nums]
sums = sum(nums)
average = sums / len(nums)
print(f''' The sum of the list is {sums} and the average of the list is {average}''')

