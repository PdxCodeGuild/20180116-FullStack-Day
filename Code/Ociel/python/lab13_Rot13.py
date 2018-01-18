
# Version 2

alpha = 'abcdefghijklmnopqrstuvwxyz'
user_word = input("Please enter a word to encode: ")
user_number = int(input("Enter the amount of rotations (Num 1 - 26): ")) - 1

x = 0
num = 0
my_string = ''

while x < len(user_word):
    newNumber = alpha.find(user_word[num])
    newNumber += user_number

    if newNumber > 26:
        newNumber = newNumber % 27

    my_string += alpha[newNumber]

    x +=1
    num += 1

print(f' Your new encryption is : {my_string} ')
