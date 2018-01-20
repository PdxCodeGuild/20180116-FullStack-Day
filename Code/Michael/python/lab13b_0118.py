

def rot(x):

    x = int(input('> Type the rotation amount. \n> '))

    instring = input('> Type something. \n> ')

    result = ""

    for i in instring:
        chars = ord(i)
        if chars >= ord('a') and chars <= ord('z'):
            if chars > ord('m'):
                chars -= x
            else:
                chars += x
        result += chr(chars)

    print(result)

rot(13)
