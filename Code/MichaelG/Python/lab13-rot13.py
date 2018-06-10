def rot13(text):
    result = ""

    for letters in text:

        convert = ord(letters)
        if convert >= ord('a') and convert <= ord('z'):
            if convert > ord('m'):
                convert -= 13
            else:
                convert += 13
        elif convert >= ord('A') and convert <= ord('Z'):
            if convert > ord('M'):
                convert -= 13
            else:
                convert += 13

        result += chr(convert)

    return result


test = input("Please enter a word to encode: ")
print(rot13(test))
