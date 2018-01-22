nums = []

# counter = 0

# loop over the elements
# for num in nums:
#    print(num)
#    counter += num
# print(counter)
# print('The average of the list of numbers is ' + str(counter/len(nums)))

enter_number = ''
while enter_number != 'done':
    enter_number = input('Enter a number or "done": ')
    if enter_number != 'done':
        nums.append(int(enter_number))
print(nums)
print('The average of the list of numbers is ' + str(sum(nums)/len(nums)))






