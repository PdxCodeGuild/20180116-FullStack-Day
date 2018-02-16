

def school():

    grade = int(input('What percentage did you get on your test? '))

    if grade >= 90:
        print('You got an A')

    elif grade >= 80:
        print('You got a B')

    elif grade >= 70:
        print('You got a C')

    elif grade >= 60:
        print('You got a D')

    else:
        print('You failed')

school()