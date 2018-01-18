print("Let's find more averages")
nums = []
numbers = (input("Please type a number\n:"))
nums.append(numbers)
while numbers != 'done':
    numbers = (input("Please type a number or done\n:"))
    nums.append(numbers)#adds numbers from input to the list nums
    if numbers == 'done':
        nums.pop()#eliminates the last item in the list
        break

nums = [int(i) for i in nums] #converts the strings in the list into integers --- still not completely sure how this works
sums = sum(nums)
average = sums / len(nums)
print(f''' The sum is {sums} and the average is {average}''')