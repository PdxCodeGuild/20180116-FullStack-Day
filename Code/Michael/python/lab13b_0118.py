instring = input('> Type something. \n> ')

x = int(input('> Type the rotation amount. \n> '))

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





















# def rot13(instring):
# print(rot13('hello'))























'''elif characters >= ord('A') and c <= ord('Z'):
if characters > ord('M'):
    characters -= x
else:
    characters += x'''