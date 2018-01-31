"""
Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for
computing the U.S. grade level for a given block of text
"""

import string  # to get a list of all the characters not in a word, such as "!@#$%^&*()[]{}"
import re

# nameoffile = input('what is the name of the file that you would like the ARI computed for (add .txt): ')
nameoffile = '80days.txt'

with open(nameoffile) as f:  # open the file. file was downloaded and added to repository
    #contents = f.readlines()  # list of all the lines as strings (not sentences)
    contents = f.read()  # list of all the lines as strings (not sentences)

punctuation = '\'\"\\/-_+=[]'

for p in punctuation:
    contents = contents.replace(p, '')

#  split full body into sentences

allsentences = re.split('[?!.]', contents)

# remove the \n
for i in range(len(allsentences)):
    allsentences[i] = allsentences[i].replace('\n', '')
# print(allsentences)

#  create a new list with the number of words in the sentence
wordsinsent = []
for i in range(len(allsentences)):
    if allsentences[i].count(' ') > 0:
        wordsinsent.append(allsentences[i].count(' ') + 1)

# 'b' is (words / sentence) * .5
b = (sum(wordsinsent) / (len(wordsinsent)))  *0.5

# split contents around each word, putting them into a list, and then finding the length
allwords = re.split('[?!. ]', contents)
# print(b)

# remove the \n
for i in range(len(allwords)):
    allwords[i] = allwords[i].replace('\n', '')
# print(allwords)


#create a new list with the numbers of characters in a sentence
charinword = []
for i in range(len(allwords)):
    if len(allwords[i]) > 0:
        charinword.append(len(allwords[i]))
# print(charinword)

a = 4.71 * (sum(charinword)/len(charinword))
# print(a)

ARI = a + b - 21.43

intARI = ARI // 1
print(ARI)

#if it's a decimal always ROUND UP
if intARI != ARI:
    ARI = int(ARI) + 1
# print(ARI)

#Use a dictionary to find the right index:
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

print(f'the ARI for {nameoffile} is {ARI} which corresponds to the following: {ari_scale[ARI]}')












#     sumsentences += len(allsentences[i])
# avgsenlen = int((sumsentences) / len(allsentences))
# print(avgsenlen)


# sentences = []
# for i in range(len(contents)):
#     sentences[i] =
#
#
#
# #split full body into words
#
#
#


# newlist = []
# for i in range(len(contents)):
#     if len(contents[i]) > 2:
#         newlist.append(contents[i])
# contents = newlist


# print(len([line for line in contents if line == '']))



#contents = [line for line in contents if len(line) > 2]






#count
#find all is a regex


# print(contents)  # test to print
#
# allsentences = re.split('[?!.]', contents)
# # print(allsentences)  # check
#
# wordcount = []
# for line in contents:
#     print(line)
#     wordcount.append(line.split(' '))
# # print(wordcount)
#
# totalsentencecount = len(allsentences)
# print(totalsentencecount)

# calculate the number of words
# words =[]
# for i in range(len(allsentences)):
#     words =


# charperline = 0
# spaces = 0
# for i in range(len(allsentences)):
#     for char in range(len(allsentences[i])):
#         if char == ' ':
#             spaces += 1
#         if char == string.ascii_letters():
#             charperline += 1



# allwords = [x for x in contents.split(' ')]  # creating a list with every words split by spaces
# #print(allwords)
#
#
# # Use for loops to remove spaces, punctuation, and blanks
# for i in range(len(allwords)):  # here we're iterating by index, whereas ...
#     allwords[i] = allwords[i].lower()
#     for char in string.punctuation:  # here we're iterating by character in a string
#         allwords[i] = allwords[i].replace(char, '')

