nums = [5, 0, 8, 3, 4, 1, 6]

counter = 0
# loop over the elements
for num in nums:
    print(num)
    counter += num
print(counter)
print(counter/len(nums))

# loop over the indices
for i in range(len(nums)):
    print(nums[i])


