def encrypt(string, x):

    # Make index of alphabet
    index = 'abcdefghijklmnopqrstuvwxyz '

    # Make an empty string to store our encrypted letters in
    rot13 = ''

    # Loop through our string
    for i in range(0, len(string)):
        num = index.find(string[i])     # Get corresponding numerical value of our letter
        if 0 <= num < 25 - x:               # Separate character in first 13
            new_num = num + x           # Rotate character's numerical value by 13
            new_char = index[new_num]     # Find corresponding character for numerical value using our index
            rot13 = rot13 + new_char     # Add new character to our string
        elif 25 - x <= num < 26:            # Same thing as above for characters in last 13
            y = 26 - num
            new_num = x - y
            new_char = index[new_num]
            rot13 = rot13 + new_char
        else:                           # Separate condition for the space character
            rot13 = rot13 + ' '         # Add space character to our string

    print(rot13)                        # Print our encrypted string


phrase = input('Input a string you would like to encrypt: ')
rot = int(input("How much would you like to rotate? "))

