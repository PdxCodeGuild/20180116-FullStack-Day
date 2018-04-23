# user_op = input("What operation would you like to perform?\n:")
# user_op = user_op.lower()
# user_num1 = input("What is the first number?\n:")
# user_num1 = float(user_num1)
# user_num2 = input("What is the second number?\n:")
# user_num2 = float(user_num2)
#
#
# if user_op in ['+', 'add', 'addition']:
#     print(user_num1 + user_num2)
# elif user_op in ['subtract', 'subtraction']:
#     print(user_num1 - user_num2)
# elif user_op in ['multiply', 'multiplication']:
#     print(user_num1 * user_num2)
# elif user_op in ['divide', 'division']:
#     print(user_num1 / user_num2)
#wrap in int
operation = input('What operation is to be done?')
first_num = int(input('What is the first number?'))
second_num = int(input('What is the second number?'))


if operation == '+':
    print(first_num,"+",second_num,"=", first_num + second_num)
elif operation == '-':
    print(first_num,"-",second_num,"=", first_num - second_num)
elif operation == '*':
    print(first_num,"*",second_num,"=", first_num * second_num)
elif operation == '/':
    print(first_num,"/",second_num,"=", first_num / second_num)
else:
    print('Please select operation and numbers.')
