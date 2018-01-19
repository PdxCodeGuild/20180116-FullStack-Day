
def code(text):
    message = []
    abc = 'abcdefghijklmnopqrstuvwxyz'
    rot = 'nopqrstuvwxyzabcdefghijklm'
    for i in text:
        x = abc.find(i) #sets the rot to the corresponding abc
        y = rot[x] # sets the variable y to the rot equivalent of abc
        message.append(y) #pulls the input from y into message
    message = ''.join(message) #marries all of the letters together

    print(message)

text = input("Give me something to make super secret\n:")
secret = code(text)
print(secret)


