# Problem 1
def is_even(my_number):
    if my_number % 2 == 0:
        return True
    else:
        return False


print(is_even(4))
print(is_even(5))


# Problem 2
# def is_opposite(num1, num2):
#
#     if num1 > 0 and num2 < 0 and num2 <= 0:
#         return True
#     if num2 > 0 and num1 < 0 and num1 <= 0:
#         return  True
#     return False
#
#
# print(is_opposite(10, -1))
# print(is_opposite(2, 3))
# print(is_opposite(-1, 9))


# Problem 3

# def near_100(number):
#     x = 90
#     while x <= 110:
#         if number == x:
#             return True
#         x += 1
#
#     return False
#
# print(near_100(50))
# print(near_100(99))
# print(near_100(105))

# Problem 4

#
# def maximum_of_three(one, two, three):
#    return max(one, two, three)
#
# print(maximum_of_three(5, 6, 2))
# print(maximum_of_three(-4, 3, 10))

# Problem 5
#
# def to_the_power(multiplier, power):
#     times = 2
#     x = 1
#     print('1,')
#     for x in range(power):
#         if x < power - 1:
#             print(f'{multiplier}, ')
#             multiplier *= times
#             x += 1
#         else:
#             print(f'{multiplier}')
#
#
# to_the_power(2, 20)
