import os
import string

# The score is computed by multiplying the number of characters divided
#  by the number of words by 4.17, adding the number of words divided by
# the number of sentences multiplied by 0.5, and subtracting 21.43. **If the
# result is a decimal, always round up.**



with open('Frankenstein.txt', 'r') as frankenstein_file:
        contents = frankenstein_file.read()

# Make everything lowercase, strip punctuation, split into a list of words.
words = contents.lower().split()

word_count = len(words)

sentence_list = contents.split('.')
print(sentence_list)

sentence_count = len(sentence_list)
print(sentence_count)
print(word_count)

character_list = []

for i in range(len(contents.strip(string.punctuation))):
    character_list.append(contents[i])
print(character_list)

character_count = len(character_list)
print(character_count)

score = ((float(character_count) / float(word_count)) * 4.17)  + 0.5 * (float(word_count) / (float(sentence_count))) - 21.43

print('score', score)  # Still need to round score up and add condition that if it is over 14 it should still be read as 14.

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


def remove_punct(text):
    return [w.strip(string.punctuation) for w in words] # Need to understand this better. What about translate?

words = remove_punct(words)
words_copy = words.copy()

print(words)

word_dictionary = {}

for i in range(len(words)):
    if words[i] not in word_dictionary.keys():
        word_dictionary[words[i]] = 1
    else:
        word_dictionary[words[i]] += 1


print(word_dictionary)


words = list(word_dictionary.items()) # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])