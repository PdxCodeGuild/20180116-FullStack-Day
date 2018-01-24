"""
Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of
eachother, False if they're not. The procedure for comparing the two strings is as follow:
"""

def check_anagram(a1,b1):
    #Convert each word to lower case (lower)
    a = a1.lower()
    b = b1.lower()

    #Remove all the spaces from each word (replace)
    a = a.replace(" ", "")
    b = b.replace(" ", "")

    #Sort the letters of each word (sorted)
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))

    # b = sorted(b)

    #Check if the two are equal
    if a == b:
        print('"' + a1 + '"' + ' and ' + '"' + b1 + '"' + ' are anagrams')
    else:
        print('"' + a1 + '"' + ' and ' + '"' + b1 + '"' + ' are NOT anagrams')


    #check
    #print(a) #test
    #print(b) #test

check_anagram(input("enter the first word: "), input("enter the second word: "))