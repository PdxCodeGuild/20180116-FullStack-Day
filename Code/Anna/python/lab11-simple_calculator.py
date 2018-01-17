"""
Lab 11
Let's calculate!
"""

print("Welcome to the calculator! What is the operation you want to perform?\n")

while True:
    print("Choose +, -, *, or /. Type 'done' to finish.")
    operation = input("> ")

    if operation == "done": # exit the loop
        break

    if operation == "+":
        print("What is the first number?")
        number1 = input("> ")

        try:
            num1 = float(number1)
        except ValueError:
            print("Not a number!")
            continue

        print("What is the second number?")
        number2 = input("> ")

        try:
            num2 = float(number2)
        except ValueError:
            print("Not a number!")
            continue

        total = num1 + num2
        print(f"The total is: {total}")

    elif operation == "-":
        print("What is the first number?")
        number1 = input("> ")

        try:
            num1 = float(number1)
        except ValueError:
            print("Not a number!")
            continue

        print("What is the second number?")
        number2 = input("> ")

        try:
            num2 = float(number2)
        except ValueError:
            print("Not a number!")
            continue

        total = num1 - num2
        print(f"The total is: {total}")

    elif operation == "*":
        print("What is the first number?")
        number1 = input("> ")

        try:
            num1 = float(number1)
        except ValueError:
            print("Not a number!")
            continue

        print("What is the second number?")
        number2 = input("> ")

        try:
            num2 = float(number2)
        except ValueError:
            print("Not a number!")
            continue

        total = num1 * num2
        print(f"The total is: {total}")

    elif operation == "/":
        print("What is the first number?")
        number1 = input("> ")

        try:
            num1 = float(number1)
        except ValueError:
            print("Not a number!")
            continue

        print("What is the second number?")
        number2 = input("> ")

        try:
            num2 = float(number2)
        except ValueError:
            print("Not a number!")
            continue

        total = num1 / num2
        print(f"The total is: {total}")

    else:
        print("Invalid operation")








