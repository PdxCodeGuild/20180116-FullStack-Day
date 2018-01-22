oper = input("what is the operation you'd like to perform?+ - * /：")
first = float(input("what is the first number?: "))
second = float(input("what is the second number?: "))

if oper == '+':
    print(first + second)
elif oper == '-':
    print(first - second)
elif oper == '*':
    print(first * second)
elif oper == '/':
    print(first / second)
else:
    print("do not have the operator")
