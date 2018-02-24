"""
Lab 22: Compute Automated Readability Index
"""
import string

dictionary = dict()
list = []
puncs = ['?', '.', '!']
sentences = 0
char_total = 0
word_total = 0
# ARI scale
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
word_chars = str(string.ascii_letters) + str(string.digits) + '-' + ' '

openbook = 'Lab22metamorphosis.txt'

# Count sentences, words and characters in text
with open(openbook, 'r') as word_file:
    for line in word_file:
        # make lowercase
        line = line.strip().lower()
        for char in line:
            if char not in word_chars and char not in puncs: # Remove punctuation
                line = line.replace(char, '')

        # count words/sentences/characters
            for word in line.split():
                char_total += len(word)
                word_total += 1
                if word[-1] in puncs and word:
                    sentences += 1

"""The score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
"""

# char_total / word_total * 4.17 + word_total / sentences * 0.5 - 21.43
ari = char_total / word_total * 4.17 + word_total / sentences * 0.5 - 21.43
#ari = 4.17 * (char_total) / word_total) + 0.5 * (word_total) / sentences) - 21.43)

# over 14 = college
college_level = 14
if ari > 14:
    ari = 14

print('Sentences: ', sentences)
print('Total words: ', word_total)
print('Characters: ', char_total)
print('ARI: ', ari)
print('The ARI for Metamorphosis is ' + str(round(ari)))


