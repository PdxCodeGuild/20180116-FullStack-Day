
#####################################################################

# def is_even(my_number):
#     return my_number % 2 == 0

# print(is_even(5))
# print(is_even(6))

#####################################################################

# def opposite(a, b):
#
#     if a > 0 and b < 0:
#         return True
#     elif a < 0 and b > 0:
#         return True
#     else:
#         return False
#
# print(opposite(10, -1))
# print(opposite(2, 3))
# print(opposite(-1, -1))

#####################################################################

# def near_100(num):
#
#     if num >= 90 and num <= 110:
#         return True
#     else:
#         return False
# #
# print(near_100(50))
# print(near_100(99))
# print(near_100(105))

#####################################################################

# def maximum_of_three(a, b, c):
#     return max(a, b, c)
#
# print(maximum_of_three(5,6,2))
# print(maximum_of_three(-4,3,10))

#####################################################################

# def powered(x):
#
#     i = 0
#     while i <= 20:
#         print(x ** i)
#         i += 1
#
# powered(2)

#####################################################################

# userText = input('Enter something here. \n> ')
# newText = ''
# i = 0
#
# while i < len(userText):
#     newText = userText[i] * 2
#     i += 1
#     print(newText, end="")

#####################################################################

# def missing_char(word):
#
#     word = 'kitten'
#
#     list = []
#     for i, x in enumerate(word):
#         list.append(word.replace(x, ''))
#     return list
#
# print(missing_char('kitten'))

#####################################################################

# latest_letter = 'pneumonoultramicroscopicsilicovolcanoconiosis'
# print(max(latest_letter))

#####################################################################

# def occurrences(sentence):
#     occurrs = sentence.count('hi')
#     return occurrs
#
# print(occurrences('hihi'))

#####################################################################

# def cat_dog(x):
#     if x.count('cat') == x.count('dog'):
#         return True
#     else:
#         return False
#
# print(cat_dog('catdog'))
# print(cat_dog('catcat'))
# print(cat_dog('catdogcatdog'))

#####################################################################

# add to functions, but it works for now

# letter = 'i'
# word = 'antidisestablishmentterianism'
#
# counted = word.count(letter)
# print(counted)
#
# letter = 'p'
# word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
#
# counted = word.count(letter)
# print(counted)

#####################################################################

# def lower_case(word):
#
#     word = ''.join(word.split())
#     return word.lower()
#
# print(lower_case("SUPER!"))
# print(lower_case("        NANNANANANA BATMAN        "))






