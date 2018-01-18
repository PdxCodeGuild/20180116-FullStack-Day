# Version 2

alpha = 'abcdefghijklmnopqrstuvwxyz'
user_word = input("Please enter a word to encode: ").lower()
user_number = int(input("Enter the amount of rotations (Num 1 - 26): ")) - 1

i = 0
my_string = ''

while i < len(user_word):

    newNumber = alpha.find(user_word[i])
    if user_word[i].islower():
        newNumber += user_number

        if newNumber > 25:
            newNumber = newNumber % 26

        my_string += alpha[newNumber]
    else:
         my_string += user_word[i]

    i += 1

print(f' Your new encryption is : {my_string} ')
