#Version 1
# nums = [5, 0, 8, 3, 4, 1, 6]
# x = sum(nums)
# y = len(nums)
# print(x/y)
#-----------------------------------------------

#Version 2

numbers = []
numinput = ''
# print(numbers)

while True:

    if numinput != 'done':

        numinput = input('Please input a number or enter done. ')
        numbers.append(numinput)
        print(numbers)
    elif numinput == 'done':
        break
numbers.pop()
numsum = sum(int(i) for i in numbers)
numlen = len(numbers)
numavg = numsum/numlen

print(numsum) #sum test
print(f"The average of your numbers is: ", {numavg})



