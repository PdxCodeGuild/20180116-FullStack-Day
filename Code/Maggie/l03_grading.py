print('Convert your percentage score to a letter grade! \n')
Percent = input('Enter the percentage score (0-100):')

def convert():
    print('You recieved ', end='')
    try:
        if int(Percent) < 60:
            print('an F', end='')
        elif int(Percent) >= 60:
            if 60 < int(Percent) < 70:
                print('a D', end='')
            elif 70 <= int(Percent) < 80:
                print('a C', end='')
            elif 80 <= int(Percent) < 90:
                print('a B', end='')
            elif int(Percent) >= 90:
                print('an A', end='')
            if int(Percent) < 100:
                if int(Percent) % 10 <= 3:
                    print('-.')
                elif int(Percent) % 10 >= 7:
                    print('+.')
                else:
                    print('.')
            else:
                print('+.')
    except:
        print('an error. Please enter a valid entry for a grade score.')

convert()
print('\n')

