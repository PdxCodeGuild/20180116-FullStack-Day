
with open('pg4.txt', 'r') as address:
    contents = address.read()

contents = contents.replace('\n', ' ')
sentences = contents.split('.?!')

table = contents.maketrans(",.?!*#/;:", 9 * " ")
contents.translate(table)
words = contents.split()

char = []
for i in range(len(words)):
    char += words[i]

score = 4.71 * (len(char) / len(words)) + 0.05 * (len(words) / len(sentences)) - 21.43
score = int(score)

if score > 14:
    score = 14

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

print(f"The ARI for gettysburg-address.txt is {score} This corresponds to a {ari_scale[score]['grade_level']} level of difficulty \nthat is suitable for an average person {ari_scale[score]['ages']} years old.")