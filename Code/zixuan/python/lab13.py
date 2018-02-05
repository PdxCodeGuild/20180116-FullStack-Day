def transfer(inputs, n):

    return chr(inputs + 95 + int(n))


inputs = input("please enter your number list with commom:")
inputs = inputs.split(",")
n = int(input("please enter your rot:"))

for i in range(len(inputs)):
    inputs[i] = transfer(int(inputs[i]), n)

print(inputs)

