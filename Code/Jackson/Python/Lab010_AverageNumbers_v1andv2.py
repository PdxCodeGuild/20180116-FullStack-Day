"""
We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum',
then divide that sum by the number of elements in that list. Remember len will give you the length of a list.
"""

#Ask the user for numbers and append each one to the list

nums = []
newnumber = 0

newnumber = (input('enter a number to the list and I will average them! (type "done" to get average): '))
while newnumber != 'done':
    nums.append(newnumber)
    newnumber = (input('enter a number to the list and I will average them! (type "done" to get average): '))


# while True:
#     newnumber = input('enter a number or done: ')
#     if newnumber == 'done':
#         break
#     else:
#         nums.append(int(newnumber))




#for loop that goes through the array and sums the numbers

sum = 0
for num in nums:
    sum += int(num)


#average the numbers

avg = sum / len(nums)


#print the average

print('the average is ' + str(avg))