# Make index of alphabet
index = 'abcdefghijklmnopqrstuvwxyz '

# Input for the string we wish to encrypt
string = input('Input a string to encrypt: ')

# Make an empty string to store our encrypted letters in
rot13 = ''

# Loop through our string
for i in range(0, len(string)):
    num = index.find(string[i])     # Get corresponding numerical value of our letter
    if 0 <= num < 13:               # Separate character in first 13
        newnum = num + 13           # Rotate character's numerical value by 13
        newchar = index[newnum]     # Find corresponding character for numerical value using our index
        rot13 = rot13 + newchar     # Add new character to our string
    elif 13 <= num < 26:            # Same thing as above for characters in last 13
        newnum = num - 13
        newchar = index[newnum]
        rot13 = rot13 + newchar
    else:                           # Separate condition for the space character
        rot13 = rot13 + ' '         # Add space character to our string

print(rot13)                        # Print our encrypted string
