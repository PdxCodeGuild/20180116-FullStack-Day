
"""
This is the grading lab to convert numbers to letters
"""

#Have the user enter a number representing the grade (0-100)
GradeNumber = int(input('select a number between 0 and 100: '))

#Convert the number grade to a letter grade
if GradeNumber >= 90:
    print('A')
elif GradeNumber >= 80:
    print('B')
elif GradeNumber >= 70:
    print('C')
elif GradeNumber >= 60:
    print('D')
else:
    print('F')




