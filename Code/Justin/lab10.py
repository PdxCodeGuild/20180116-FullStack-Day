nums = []

num = input('Enter a number, \'done\' to end: ')

while num != 'done':
    while True:
        try:
            num = int(num)
            nums.append(num)
            break
        except ValueError:
            print('Enter an integer, please.')
    num = input('Enter a number, \'done\' to end: ')

s = 0.0
for i in nums:
    s += i


if len(nums) != 0:
    avg = s / len(nums)
    print(nums)
    print('The average is: ',avg)