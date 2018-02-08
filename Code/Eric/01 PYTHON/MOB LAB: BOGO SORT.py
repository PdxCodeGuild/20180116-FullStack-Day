# bogo sort
import random

# n = int(input('\nenter the number\n:'))
n = 4


def random_list(n):
	nums = []
	for i in range(n):
		nums.append(random.randint(0, 100))
	return nums


nums = random_list(n)


def shuffle(nums):
	for number in range(len(nums)):
		j = random.randint(0, len(nums) - 1)
		nums[number], nums[j] = nums[j], nums[number]


def is_sorted(nums):
	for i in range(0, len(nums) - 1):
		if nums[i] > (nums[i] + 1):
			return False
	return True


def bogo_sort(nums):
	while not is_sorted(nums):
		shuffle(nums)
		print(nums)


# print(nums)
# shuffle(nums)
# print(nums)

bogo_sort(nums)
