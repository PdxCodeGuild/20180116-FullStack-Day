##### Automated Readability Index ############
import string
import math

with open('kindergarten.txt', 'r') as f:
    contents = f.read()
    sentences = contents.split('.')
    letters = list(contents)

    for c in string.punctuation:
        contents = contents.replace(c, ' ')
    words = contents.split()

ari = 4.71 * (len(letters) / len(words)) + .5 * (len(words) / len(sentences)) - 21.43
ari = math.ceil(ari)
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

for i in ari_scale:
    if ari > 14:
        ari = 14
    if ari < 1:
        ari = 1

grade_level = ari_scale[i]['grade_level']
age_level = ari_scale[i]['ages']
print(f'''The ARI for this title is {ari}.\n This corresponds to a {grade_level} level.\n This is suitable for persons in the range of {age_level} years old.''')





print(ari)
print(sentences)
print(letters)
print(words)

