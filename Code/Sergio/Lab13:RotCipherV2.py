"Lab 13: Rot Cipher Version 1 and 2"
#Index 	 0 	   1 	2 	 3 	  4    5 	6 	 7 	  8    9 	10 	11   12   13   14 	15   16   17   18 	19 	 20   21   22 	23   24   25
#index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
#ROT13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
engls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


user_input = input('Enter a string ').lower()
print(user_input)
encrypted = ''
user_number = input('Enter number ')

for character in user_input:
    try:
        stringindex = engls.index(character)
        stringindex += int(user_number)
        if stringindex >= 26:
            stringindex -= 26
        encrypted += engls[stringindex]
    except ValueError:
        encrypted += character

print(encrypted)


