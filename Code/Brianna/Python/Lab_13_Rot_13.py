import string

input_phrase = input("Please type your word to by encrypted in Upper Case letters with no spaces or additional characters.\n:")
new_phrase = ''
alphabet_list = list(string.ascii_uppercase)
rotation = int(input("By how much would you like to rotate your cypher? Please enter a number.\n:"))

for i in range(len(input_phrase)):
    character = input_phrase[i].upper()
    index = alphabet_list.index(character)
    index += rotation
    index %= len(alphabet_list)
    new_phrase += alphabet_list[index]


print(new_phrase)

#decypher = input("Would you like to decypher your code?")
#original_phrase = ''
#print("Okay!")

'''




for i in range(len(input_phrase)):


    new_phrase = new_phrase + alphabet_list[(((alphabet_list.index(input_phrase[i].upper())) + rotation)% 26)]

if decypher == "yes" or decypher == "y":
    for i in range(len(input_phrase)):
        original_phrase = original_phrase + alphabet_list[(((alphabet_list.index(new_phrase[i].upper())) - rotation) % 26)]

print(new_phrase)

'''