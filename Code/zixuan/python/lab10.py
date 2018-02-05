nums = 0
i = 0
while True:
    inp = input(" enter a number, or 'done':")
    if inp == 'done':
        break
    inp = float(inp)
    nums += inp
    i = i + 1

ave = nums / i
print(nums)
print(ave)
