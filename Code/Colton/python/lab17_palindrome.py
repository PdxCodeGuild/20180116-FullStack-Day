user = input("Give me a word\n:")
user = list(user)
palindrome = user[::-1] #reverse the user input
if user == palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")


###anagram###
def sort_word():
    user = input("Enter a word\n:")
    user = user.replace(' ', '')
    user = list(user)
    user = sorted(user)
    return user

user_1 = sort_word()
user_2 = sort_word()

if user_1 == user_2:
    print("Its an anagram")
else:
    print('This is not an anagram')



