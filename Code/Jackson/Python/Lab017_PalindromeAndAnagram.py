"""
Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False
if it's not.

"""

#get user input

word = input("Enter a word: ")

#count the number characters in the word
length = len(word)

#create a list which all the individual characters as elements
list = []
i = 0
while i < length:
    list.append(word[i])
    i += 1

#write a loop with the number of the characters needs to check, use //2
j = length//2 #figure out how many times to run through the loop
i = 0
k = -1
while i < j:
    if list[i] == list[k]: #if statement that either prints it is or is not a palindrome
        k -= 1
        i += 1 #increment i by one
        if i == j:
            print('"' + word +'"' + " is a palindrome!")
            break
    else:
        print('"' + word + '"' + " is not a palindrome")
        break




