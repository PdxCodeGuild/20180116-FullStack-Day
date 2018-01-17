'''
Madlibs
'''

print('let\'s try a madlib! \nFollow the instructions below.')
q1 = input('Input a proper noun: ')
q2 = input('Input a verb: ')
q3 = input('Input an object: ')
q4 = input('Input a location: ')

def main():

    print('\nHere is your madlib:\nIf {word_1} would just {word_2}, \n'
          'I could finally get my {word_3} out of {word_4}.\n'.format(word_1=q1, word_2=q2, word_3=q3, word_4=q4))
main()
Again = input('would you like to try again? (Y/N): ')
if Again.upper() == 'Y':
    q1 = input('Input a proper noun: ')
    q2 = input('Input a verb: ')
    q3 = input('Input an object: ')
    q4 = input('Input a location: ')
    main()
else:
    print('Ok.')

print('\n')
print('Thanks for playing!')
