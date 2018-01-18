print("Let's fins more averages")
nums = []
numbers = (input("Please type a number\n:"))
nums.append(numbers)
while numbers != 'done':
    numbers = (input("Please type a number or done\n:"))
    nums.append(numbers)
    if numbers == 'done':
        nums.pop()
        break

print(nums)




