print('Let\'s check if a word is an anagram.')
anagram = input('Type in a word: ')

for i in range(0, len(anagram)):
    if anagram[i] != anagram[len(anagram) - 1 - i]:
        print('This word is not an anagram')
        break
    elif i == len(anagram) - 1:
        print('This is an anagram')

