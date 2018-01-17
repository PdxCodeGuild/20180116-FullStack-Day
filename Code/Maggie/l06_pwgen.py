import random
import string

from time import sleep
'''Password Generator. 2018 Maggie Geise

Generate a password of length n using a while loop and ranom.choice, this will be a string of random characters
(Hint: random.choice can be used to pick a character out of a string, as well as element on list)

Bonus: Allow the user to enter the value of n, (remember to convert its type, as input refers to a string)
'''


print('A Password Generator \n')


'''num = input('How many characters would you like your password to be?\n'
                       'Enter a numerical digit between 1-10 or anything else to let me choose.\n'
                       'Your choice: ')
'''

def generate():
    num = input('How many characters would you like your password to be?\n'
                'Enter a numerical digit between 1-10.\n'
                'Your choice: ')
    password = ''
    characters= list(string.ascii_letters + string.digits)
    try:
        pw_len =int(num)
        print(num)
    except ValueError:
        print('exception')
        print('Sorry that was not a valid entry. I will choose for you.')
        num = random.randrange(100)
        generate()
    print('Generate a password of length: ' + num)
    if pw_len <= 100:
        print('Ok.\n')
        sleep(0.5)
        print('generating your password')
        sleep(0.5)
        print('your randomly generated passkey is:\n')
        for i in range(pw_len):
            password = password + (random.choice(characters))
        print(password, '\n')
        close()
    else:
        print('Sorry that number was out of range.')
        num = input('How many characters would you like your password to be?\n'
                'Please enter a number less than 100.\n'
                'Your choice: ')


def close():
    close_query = input('Would you like me to generate another password? (Y/N)')
    if close_query.upper() == 'Y':
        num = input('How many characters would you like your password to be?\n'
                    'Enter a numerical digit between 1-10 or anything else to let me choose.\n'
                    'Your choice: ')
        return num
        generate()

    else:
        print('Ok. Thanks for using this password generator!')
        sleep(0.5)
        print('Take care.')
        # end

generate()