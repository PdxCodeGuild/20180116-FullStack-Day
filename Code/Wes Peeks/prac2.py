# Get a string from the user, print out another string, doubling every letter.

user = str(input('Your words\n:'))

def double_string(user):
        user1 = ''# empty string for return
        for char in list(user):# loop through characters by converting to list
            user1 += char * 2# user1 empty string gets characters times 2
        print(user1)


double_string(user)

#Write a function that takes a string, and returns a list of strings, each missing a different character.
s = input('Word')

def weird_string(s):
    s1 = []
    for char in list(s):
        s = list(s)
        s1 = char + s.pop(randint)

        print(s1)

weird_string(s)
