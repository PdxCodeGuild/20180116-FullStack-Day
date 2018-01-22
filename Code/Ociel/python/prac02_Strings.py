# Problem 1
x = 0
word = 'helor'
new_word = ''

while x < len(word):
    new_word += word[x] + word[x]
    x += 1

print(new_word)

#################################################################################

# Problem 2
# def missing_char(word):
#     list = []
#     for i,x in enumerate(word):
#         list.append(word.replace(x, ''))
#
#
#     return list
#
# word = 'kitten'
# print(missing_char('kitten'))


#################################################################################

# Problem 3
# Returns the word that has the highest ascii number
# which the problem wants whatever is closer to z
#
# def lattest_letter(word):
#     return max(word)
# print(f"The latest letter is {lattest_letter('abcsdefrlz')}.")
#

#################################################################################

# Problem 9
#.count() can have what you want to extract and count how many times it says it
# it doesnt matter if it has spaces.
#
# def count_hi(count_of_hi):
#
#     return count_of_hi.count('hi')
#
# the_hi_word = 'hihihihi hi'
# print(count_hi(the_hi_word))

#################################################################################

# Problem 10
#
# def cat_dog(cat_and_dog):
#     if cat_and_dog.count('cat') == cat_and_dog.count('dog'):
#         return True
#     else:
#         return False
#
#
# cat_dog_word = 'catcat'
# print(cat_dog(cat_dog_word))
#################################################################################
# Problem 7

# def count_letter(letter, word):
#     return word.count(letter)

# the_letter  = 'i'
# the_word = 'antidisestablishmentteriansim'
#
# print(count_letter(the_letter,the_word))
#
# the_letter  = 'p'
# the_word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
# print(count_letter(the_letter,the_word))

#################################################################################
# Problem 8
## lsstrip() removes whitespace from the begining part of the sentence
## rstrip() removes whitspace form the end part of the sentence
# you can stack them all together in the same variable.
#################################################################################
#
# def make_lower_case(lower_case_word):
#     return lower_case_word.lower().lstrip().rstrip()
#
# word = 'SUPER'
# print(make_lower_case(word))
#
# word = '        NANNANANANA BATMAN        '
# print(make_lower_case(word))

