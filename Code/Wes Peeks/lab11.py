user_op = input("What operation would you like to perform?\n:").lower()
user_num1 = input("What is the first number?\n:")
user_num1 = float(user_num1)
user_num2 = input("What is the second number?\n:")
user_num2 = float(user_num2)


if user_op in ['add', 'addition']:
    print(user_num1 + user_num2)
elif user_op in ['subtract', 'subtraction']:
    print(user_num1 - user_num2)
elif user_op in ['multiply', 'multiplication']:
    print(user_num1 * user_num2)
elif user_op in ['divide', 'division']:
    print(user_num1 / user_num2)
