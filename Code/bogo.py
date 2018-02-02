import random

n = int(input('What is the length of the list of numbers?\n:'))



def random_list(n):
    random_list = []
    for i in range(n):
        random_list.append((random.randint(0, 100)))
    return random_list

nums = random_list(n)

def indicception(nums):
    for i in range(len(nums)):
        j = random.randint(0, len(nums))
        nums[i], nums[j] = nums[j], nums[i]

def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def bogo_sort(nums):
    while is_sorted == False:
        indicception(nums)



