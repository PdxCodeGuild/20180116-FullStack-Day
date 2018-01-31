import string
import math

word_pairs_dictionary = dict()
long_word_list = []



word_chars = str(string.ascii_letters) + str(string.digits) + '-' + ' '
mr_mrs_ms = ['mr.', 'mrs.', 'ms.']
sentence_end = ['.', '?', '!']

sentence_count = 0
character_count = 0
word_count = 0

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

file_name = input('File name please?')

# Count sentences, words and characters in text
with open(file_name, 'r') as word_file:
    for line in word_file:
        line = line.strip().lower()  # For line strip whitespace and make lowercase
        for char in line:
            if char not in word_chars and char not in sentence_end: # Remove all punctuation except '.?!'
                line = line.replace(char, '')

        # Count characters, words, and sentences
        for word in line.split():
            character_count += len(word)
            word_count += 1
            if word[-1] in sentence_end and word not in mr_mrs_ms:
                sentence_count += 1




print('Sentences: ', sentence_count)
print('Words: ', word_count)
print('Characters: ', character_count)

ari = math.ceil(4.74 * (float(character_count) / word_count) + .5 * (float(word_count) / sentence_count) - 21.43)

if ari > 14:
    ari = 14

print('ARI: ', ari)

print(f'The ARI for {file_name} is', ari)
print('This corresponds to', ari_scale[ari]['grade_level'], 'Reading Level')
print('Suitable for students age', ari_scale[ari]['ages'])
