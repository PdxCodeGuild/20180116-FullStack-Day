print('Convert your percentage score to a letter grade! \n')
Percent = input('Enter the percentage score (0-100):')


def convert():
    print('You recieved ', end='')
    try:
        if int(Percent) < 60:
            print('an F.')
        elif 60 < int(Percent) < 70:
            print('a D.')
        elif 70 <= int(Percent) < 80:
            print('a C.')
        elif 80 <= int(Percent) < 90:
            print('a B.')
        elif int(Percent) >= 90:
            print('an A.')
    except:
        print('an error. Please enter a valid entry for a grade score.')

convert()
print('\n')

