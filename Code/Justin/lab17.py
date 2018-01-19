def check_palindrome():
    word = input('Enter the word: ')
    if word == word[::-1]: # Check if word is equal to word backwards
        print('This is a palindrome')
    else:
        print('This is not a palindrome')

def check_anagram():
    words = []
    for i in range(2):
        words.append(input(f'Enter word {i + 1}: '))
    if sorted(words[0]) == sorted(words[1]): # Check if the two words sorted are equal
        print('These are anagrams')
    else:
        print('These are not anagrams')



print('You can \n1) check for anagram \n2) check for a palindrome \n3) quit')
choice = int(input('Enter your choice. '))

while choice != '3':
    while True:
        try:
            choice = int(choice)
            choice = (choice % 3) # Lets user input any integer which is then reduced mod 3 to a valid choice
            break
        except ValueError:
            choice = input('Please enter 1, 2 or 3.')

    if choice == 1:
        check_anagram()

    elif choice == 2:
        check_palindrome()

    else:
        break

    choice = int(input('Enter your choice. '))


print("Thank you for playing. Have a nice day.")
