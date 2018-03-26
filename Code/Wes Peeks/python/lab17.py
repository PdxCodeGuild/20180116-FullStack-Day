user1 = input("Put a word here.\n:")
check = user1[::-1]

if user1 == check:
    print("You are a drome.")
else:
    print('NOPE NOPE NOPE')



def anagram(first, second):
    is_anagram = False
    f_word = sorted(first.lower().replace(' ',''))
    s_word = sorted(second.lower().replace(' ',''))

    if len(f_word) != len(s_word):
        print(f'\'{first}\' and \'{second}\' not anagrams')
    else:
        for i in range(len(f_word)):
            if f_word[i] == s_word[i]:
                is_anagram = True
            else:
                is_anagram = False

    if is_anagram:
        print(f'\'{first}\' and \'{second}\' are anagrams')

    return


first = input('First word.')
second = input('Second word.')
anagram(first, second)