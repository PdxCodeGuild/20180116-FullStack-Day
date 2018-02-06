
inputs = input("please enter your word:")
n = int(input("please enter your rot:"))
tmp = list(inputs)
for i in range(len(inputs)):
    newChr = ord(inputs[i])+n
    if newChr > 122:
        newChr = newChr -122 + 96



    tmp[i] = chr(newChr)

print(''.join(tmp))

