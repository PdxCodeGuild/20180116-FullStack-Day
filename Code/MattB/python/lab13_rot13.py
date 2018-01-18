index = 'abcdefghijklmnopqrstuvwxyz '

string = input('Input a string to encrypt: ')

rot13 = ''

for i in range(0, len(string)):
    num = index.find(string[i])
    if 0 <= num < 13:
        newnum = num + 13
        newchar = index[newnum]
        rot13 = rot13 + newchar
    elif 13 <= num < 26:
        newnum = num - 13
        newchar = index[newnum]
        rot13 = rot13 + newchar
    elif num == 26:
        rot13 = rot13 + ' '

print(rot13)
