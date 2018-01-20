def rot(y):

    lists = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    x = int(input('> Type the rotation amount. \n> '))

    instring = input('> Type something. \n> ')

    result = ""
    for i in lists:

        chars = ord(i)
        if chars in lists:
            if 'a' <= char <= 'm' or 'A' <= char <= 'M':
                char = chr(x + y)
            elif 'n' <= char <= 'z' or 'N' <= char <= 'Z':
                char = chr(x - y)
            result = result + char

        result += chr(chars)

    print(result)

rot(13)





# import string
#
#
# def rot(y):
#
#     x = int(input('> Type the rotation amount. \n> '))
#
#     instring = input('> Type something. \n> ')
#
#     result = ""
#     for i in instring:
#
#         chars = ord(i)
#         if chars in string.ascii_letters:
#             if chars <= 'm':
#                 chars = chr(x + y)
#             else:
#                 chars = chr(x - y)
#             result = result + chars
#
#         result += chr(chars)
#
#     print(result)
#
# rot(13)
