import os
import string
import math

# Open the document...and close it with with open. ^^
with open('Frankenstein.txt', 'r') as frankenstein_file:
        contents = frankenstein_file.read()


# Make everything lowercase, strip punctuation, split into a list of words.
words = contents.lower().split()
# Word count
word_count = len(words)

# Make sentence list by splitting sentences by the '.'
sentence_list = contents.split('.')
sentence_count = len(sentence_list)

# Make a character list.
character_list = []

for i in range(len(contents.strip(string.punctuation))):
    character_list.append(contents[i])

# And count the characters
character_count = len(character_list)

# figure out a rough score
score = ((float(character_count) / float(word_count)) * 4.17)  + (0.5 * (float(word_count) / (float(sentence_count)))) - 21.43

if score > 14:
    score = 14
else:
    score = math.ceil(score)

print('score', score)

ari_scale = {
    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages': '6-7', 'grade_level': '1st Grade'},
    3: {'ages': '7-8', 'grade_level': '2nd Grade'},
    4: {'ages': '8-9', 'grade_level': '3rd Grade'},
    5: {'ages': '9-10', 'grade_level': '4th Grade'},
    6: {'ages': '10-11', 'grade_level': '5th Grade'},
    7: {'ages': '11-12', 'grade_level': '6th Grade'},
    8: {'ages': '12-13', 'grade_level': '7th Grade'},
    9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
}

# make the output
print(f"The ARI for Frankenstein is {score}. \n This corresponds to a {ari_scale[score]['grade_level']} level of difficulty \n that is suitable for an average person {ari_scale[score]['ages']} years old.")

'''
   The ARI for gettysburg-address.txt is 12
    This corresponds to a 11th Grade area of difficulty
    that is suitable for an average person 16-17 years old.
'''
