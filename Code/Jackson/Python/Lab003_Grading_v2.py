"""
Find the specific letter grade (A+, B-, etc).

"""

#80-82 = 'B-'
#83-86 = 'B'
#87-89 = 'B+'


grade = int(input("enter the percentage that you received and I will determine the grade: "))

#Convert the number grade to a letter grade
if grade >= 97:
    print('A+')
elif grade >= 93:
    print('A')
elif grade >= 90:
    print('A-')
elif grade >= 87:
    print('B+')
elif grade >= 83:
    print('B')
elif grade >= 80:
    print('B-')
elif grade >= 77:
    print('C+')
elif grade >= 73:
    print('C')
elif grade >= 70:
    print('C-')
elif grade >= 67:
    print('D+')
elif grade >= 63:
    print('D')
elif grade >= 60:
    print('D-')
else:
    print('F')