"""
Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication,
and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can
convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample
input/output.
"""

while True:
    #get the user input and convert to a float
    operator = input('what is the operation that you would like to perform?: ')
    if operator == 'done':
        print('goodbye')
        break

    #version 2: go until user says "done"

    #get the first number
    user_input_first_number = input('what is the first number?: ')
    first_number = float(user_input_first_number)


    #get the second number
    user_input_second_number = input('what is the second number?: ')
    second_number = float(user_input_second_number)



    #Calculate answer
    if operator == '+': #since the operator variable is a representation of the operator, need to do if statement
        answer = first_number + second_number
    elif operator == '-':
        answer = first_number - second_number
    elif operator == '*':
        answer = first_number * second_number
    elif operator == '/':
        answer = first_number / second_number
    else:
        print('could not calculate, please try again')

    #print
    print(answer)