####Super easy peasy calculator :-)###
print("Super fun calculator time!")
functions = ('add', 'subbtract', 'divide', 'multiply')
ops = input("What is your operation?\nAdd\nSubtract\nDivide\nMultiply\n:").lower()
while ops not in functions:
    ops = input("What is your operation?\nAdd\nSubtract\nDivide\nMultiply\n:").lower()
while True:
    try:
        x = float(input("What is your first number?\n:"))
    except ValueError:
        continue
    else:
        break

while True:
    try: #if anything in the try loop causes an error. The way to make a loop for catching string where an integer should be?
        y = float(input("What is your second number?\n:"))
    except ValueError: # if an integer or float is not entered where it should be, its a ValueError
        continue #returns control to the beggining
    else: #the try loop got what it wanted and moves along to the next code
        break


if ops == 'add':
    print(x + y)
elif ops == 'divide':
    print(x / y)
elif ops == 'subract':
    print(x - y)
elif ops == 'multiply':
    print(x * y)