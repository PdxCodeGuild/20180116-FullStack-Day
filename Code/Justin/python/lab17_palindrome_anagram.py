def check_palindrome(w):
    if w == w[::-1]: # Check if word is equal to it own reverse
        return True
    return False

def check_anagram(w1, w2):
    if sorted(w1) == sorted(w2): # Sorts the two words and checks for equality
        return True
    return False



print('You can \n1) check for anagram \n2) check for a palindrome \n3) quit')
choice = input('Enter the number of your choice. ')

while choice != '3':
    # Check to make sure user choice is valid.
    while True:
        try:
            choice = int(choice) % 3 # Lets user input any integer which is then reduced mod 3 to a valid choice
            break
        except ValueError:
            choice = input('Please enter 1, 2 or 3.')

    if choice == 1:
        words = []
        for i in range(2):  # Request 2 words from user
            words.append(input(f'Enter word {i + 1}: '))
        if check_anagram(words[0], words[1]):
            print('These are anagrams')
        else:
            print('These are not anagrams')

    elif choice == 2:
        word = input('Enter the word: ')
        if check_palindrome(word):
            print('This is a palindrome')
        else:
            print('This is not a palindrome')

    else:
        break

    choice = input('Enter your choice. ')


print("Thank you for playing. Have a nice day.")
