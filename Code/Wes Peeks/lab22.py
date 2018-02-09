import string
import math

with open('Thus Spoke Zarathrustra.txt', 'r', encoding="utf8") as book:
    contents = book.read()
    characters = list(contents)
    sentences = contents.split('.')


def read_level():
    for c in string.punctuation():
        contents.replace(c, ' ')


words = contents.split()


ari = 4.71 * (len(characters) / len(words)) + .5 * (len(words) / len(sentences)) - 21.43
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
if ari < 1:
    ari = 1
if ari > 14:
    ari =14

grade_level = ari_scale[ari]['grade_level']
age_level = ari_scale[ari]['ages']

print(f'''The ARI is {ari}.\n A reading grade at the {grade_level} level.\n Age Range {age_level} .''')


#print(words)
#print(sentences)
#print(characters)
