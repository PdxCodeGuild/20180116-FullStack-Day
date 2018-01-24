



# myStr1 = input("enter a word:\n> ")

# if myStr1 == myStr1[::-1]:
#     print(f'{myStr1} is a palindrome')
# else:
#     print(f'{myStr1} is not a palidrome')



myStr1 = input("enter a word:\n> ").lower()
myStr2 = input("enter a word:\n> ").lower()

myStr1 = myStr1.replace(" ", "")
myStr2 = myStr2.replace(" ", "")

if sorted(myStr1) == sorted(myStr2):
    print('are anagrams.')

else:
    print('are not anagrams.')


