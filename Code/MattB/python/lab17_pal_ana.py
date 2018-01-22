def palindrome(palin):
    for i in range(0, n(palin)):
        if palin[i] != palin[len(palin) - 1 - i]:
            print('This is not a palindrome.')
            break
        elif i == len(palin) - 1:
            print('This is a palindrome.')


def anagram(ana, check):
    ana = input('ana: ')
    check = input('check: ')

    n_ana = ana.lower()
    n_check = check.lower()
    n_ana = n_ana.replace(' ', '')
    n_check = n_check.replace(' ', '')
    n_ana = ''.join(sorted(n_ana))
    n_check = ''.join(sorted(n_check))

    if len(n_check) != len(n_ana):
        print('These are not anagrams.')
    else:
        for i in range(0, len(n_check)):
            if n_check[i] != n_ana[i]:
                print('These are not anagrams.')
            elif i == len(n_check) - 1:
                print('These are anagrams.')



