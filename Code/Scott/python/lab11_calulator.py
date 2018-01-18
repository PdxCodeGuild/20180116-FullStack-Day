
# declare user_operator as input(operator)
# declare user_first_number as input(first number)
# declare user_second_number as input(second number)

user_operator = input('What is the operation you want to perform? (+, -, *, /) ')
user_first_number = input('What is the first number? ')
user_sec_number = input('What is the second number? ')

# float user_first_number to convert string to float
# float user_second_number to convert string to float

user_first_number = float(user_first_number)
user_sec_number = float(user_sec_number)

# write if statement for operator
# write elif statements for other operators
# write else statement when operater is invalid

if user_operator == '+':
    print(user_first_number + user_sec_number)
elif user_operator == '-':
    print(user_first_number - user_sec_number)
elif user_operator == '*':
    print(user_first_number * user_sec_number)
elif user_operator == '/':
    print(user_first_number / user_sec_number)
else:
    print('Invalid operator')







