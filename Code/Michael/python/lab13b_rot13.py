

def rot(x):
    x = int(input('> Type the rotation amount. \n> '))     # increment amount is assigned to variable x

    instring = input('> Type something. \n> ')             # string input is assigned to variable instring

    result = ""                                            # "" is used as a placeholder to pass our converted string to result

    for i in instring:                                     # assign instring to to i and iterate over it using a for-loop

        chars = ord(i)                                     # assign our index of i through our method of ord to chars

        if chars >= ord('a') and chars <= ord('z'):        # if the unicode characters are >= to 97(ord('a')) AND <= 122 (ord('z')) evaluate the the if/else below

            if chars > ord('m'):                           # if the unicode characters are > 109(ord('m')), decrement by x
                chars -= x

            else:
                chars += x                                 # if not, increment by x

        result += chr(chars)                               # to encode the shifted characters back into text using chr and add them one by one into result

    print(result)                                          # prints result

rot(13)

