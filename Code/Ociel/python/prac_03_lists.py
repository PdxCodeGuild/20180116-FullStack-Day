import random
# Problem 1
# Random.choice() The choice function can often be used
# for choosing a random element from a list.

def random_element(word):
    return random.choice(word)

fruits = ['apples', 'bananas', 'pears']

print(random_element(fruits))

###################################################################
# Problem 2
# def enter_a_number():
#     answer = ''
#     total_numbers = []
#     while answer != 'done':
#         answer = input('Enter a number (or \'done\'): ')
#         if answer != 'done':
#             total_numbers.append(answer)
#     return total_numbers
#
#
# print(enter_a_number())

###################################################################
# Problem 3 (Still not done)

# def even_even(number):
#     compare = []
#     for i in range(len(number)):
#
#         print(i)
#
#     return
#
# number = [5, 6, 2]
#
# even_even(number)

###################################################################
# Problem 4
#
# def while_loop(number):
#     i = 0
#     while i < len(number):
#         if number[i] % 2 == 0:
#             print(number[i])
#         i += 1
#
#
# def for_loop(number):
#     for i in range(0,len(number), 2):
#         print(number[i])
#
#
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
#
# for_loop(nums)
# while_loop(nums)


###################################################################
# Problem 5
# def reverse(reverse_list):
#     return reverse_list[::-1]
#
# reverse_list = [1,2,3,4,5,6]
#
# print(reverse(reverse_list))


###################################################################
# Problem 6
# def extract_less_than_ten(nums):
#     new_list = []
#     for x,i in enumerate(nums):
#         if nums[x] >= 10:
#             new_list.append(nums[x])
#
#     return new_list
#
# less_than_ten = [10, 11, 12, 20, 2, 4, 6, 7, 9, 50]
#
# print(extract_less_than_ten(less_than_ten))

###################################################################
