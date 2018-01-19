#value = input('> Type NOW! \n> ')

dict = str.maketrans("abc", "def")
print(dict)


# Translate this value.
value = input('> Type!\n> ')
result = value.translate(dict)
print(result)