print('Let\'s check if a word is an palindrome.')
palin = input('Type in a word: ')

for i in range(0, len(palin)):
    if palin[i] != palin[len(palin) - 1 - i]:
        print('This is not a palindrome.')
        break
    elif i == len(palin) - 1:
        print('This is a palindrome.')

