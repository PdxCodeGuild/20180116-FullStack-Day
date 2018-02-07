# Get a string from the user, print out another string, doubling every letter.

# user = str(input('Your words\n:'))
import string

def double_string(user):
        user1 = ''  # empty string for return
        for char in list(user):  # loop through characters by converting to list
            user1 += char * 2  # user1 empty string gets characters times 2
        print(user1)


# double_string(user)

#Write a function that takes a string, and returns a list of strings, each missing a different character.
#s = input('Word')


def weird_string(s):
    s = input('Word')
    output = []
    for char in range(len(s)):
        s = list(s)
        s1 = s.copy()
        s1.pop(char)
        s1 = ''.join(s1)
        output.append(s1)
    print(output)

#weird_string(s)


#Return the letter that appears the latest in the english alphabet.



def alphebet_letter():
    a = string.ascii_lowercase
    word = input('Word')
    for char in a[::-1]:
        if char in word:
            return char

#print(alphebet_letter())
#Write a function that returns the number of occurances of 'hi' in a given string.



def count_hi(x, y):
    # repeat = string.input(hi)
    print(x.count(y))


repeat = input('gimmie a string: ')
count_hi(repeat, "hi")

#Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'



def cat_dog(uinput):
    if uinput.count('cat') == uinput.count('dog'):
        return True
    else:
        return False

print(cat_dog('catdogcat'))
