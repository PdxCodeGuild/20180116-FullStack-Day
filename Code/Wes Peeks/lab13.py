def blackhorse(user1):
    norm = 'abcdefghijklmnopqrstuvwxyz'
    caesar = 'nopqrstuvwxyzabcdefghijklm'
    gladius = []
    for char in user1:
        c = norm.find(char)
        r = caesar[c]
        gladius.append(r)
    gladius = ''.join(gladius)
    return gladius

user1 = input('Please enter your sentence to be encrypted.\n:')
user1 = user1.lower()
brutus = blackhorse(user1)
print(brutus)
