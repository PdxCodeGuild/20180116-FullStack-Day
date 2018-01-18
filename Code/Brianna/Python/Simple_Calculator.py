import time
go_on = True

# Make while loop
while go_on == True:
    operation = input("What operation would you like to perform? Please choose between +, -, *, and /.\n:")
    first_number = float(input("What is the first number?\n:"))
    second_number = float(input("What is the second number?\n:"))

    if operation == '+':
        answer = (first_number + second_number)
    elif operation == '-' :
        answer = (first_number - second_number)
    elif operation == '*' :
        answer = (first_number * second_number)
    elif operation == '/' :
        answer = (first_number / second_number)
    else:
        print("Sorry. Try again")

    print(f'{first_number} {operation} {second_number} = {answer}. ^_^')
    time.sleep(0.75)
    again = input("Would you like to continue? Yes or no?\n:")
    if again == 'yes' or 'y':
        go_on == True
    elif again == 'no' or 'n':
        print('Goodbye!')
        go_on == False
    else:
        print("Let's calculate something new!")



