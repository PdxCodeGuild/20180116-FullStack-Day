import random
welcome = input('Hello would you like a password?')
print('Creating password')

bet1 = ['a', 'b', 'c', 'd']
bet2 = ['e', 'f', 'g', 'h']
bet3 = ['i', 'j', 'k', 'l']
bet4 = ['m', 'n', 'o', 'p']
bet5 = ['q', 'r', 's', 't']
bet6 = ['u', 'v', 'w', 'x', 'y', 'z']

rand1 = random.choice(bet1)
rand2 = random.choice(bet2)
rand3 = random.choice(bet3)
rand4 = random.choice(bet4)
rand5 = random.choice(bet5)
rand6 = random.choice(bet6)


alphabet = 'abcdefghABCD012346789'
output = ''
output += random.choice(alphabet)
output += random.choice(alphabet)
output += random.choice(alphabet)
output += random.choice(alphabet)
output += random.choice(alphabet)
output += random.choice(alphabet)

print(output)

password = ((rand1) + (rand2) + (rand3) + (rand4) + (rand5) + (rand6))
#print(password)