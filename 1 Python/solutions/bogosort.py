# bogo sort

import random
import time

# n = int(input('Enter the number: '))
n = 10

def random_list(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(0, 100))
    return nums

nums = random_list(n)


def shuffle(nums):
    for i in range(len(nums)):
        j = random.randint(0, len(nums) - 1)
        nums[i], nums[j] = nums[j], nums[i]


def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def get_time():
    return int(round(time.time() * 1000))

def bogo_sort(nums):
    count = 0
    start_time = get_time()


    while not is_sorted(nums):
        shuffle(nums)
        count += 1

    end_time = get_time()
    time_taken = end_time - start_time
    print(f'total time taken: {time_taken/1000} seconds')
    print(f'time per step:    {time_taken/1000/count} second')
    print(f'steps:            {count}')


# print(nums)
# shuffle(nums)
# print(nums)

bogo_sort(nums)
