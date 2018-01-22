val = input ('Enter grade')
val = int(val)

if val >= 100:
    grade = 'A+'

if val >= 90:
    grade = 'A'
    if 0 <= val % 10 <= 3:
        grade += '-'
    elif 7 <= val % 10 <= 9:
        grade += '+'
elif val >= 80:
    grade = 'B'
    if 0 <= val % 10 <= 9:
        grade += '-'
    elif 7 <= val % 10 <= 9:
        grade += '+'
elif val >= 70:
    grade = 'C'
    if 0 <= val % 10 <= 9:
        grade += '-'
    elif 7 <= val % 10 <= 9:
        grade += '+'
elif val >= 60:
    grade = 'D'
    if 0 <= val % 10 <= 3:
        grade += '-'
    elif 7 <= val % 10 <= 9:
        grade += '+'
else:
    grade = 'F'

print(grade)


