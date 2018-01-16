"""
Lab 3
Let's get grading!
"""

run = "Y"

while run == "Y":
    grade = int(input("What grade did you get? "))

    if grade > 89:
        print("\nSweet, you got an A!")
    elif grade > 79:
        print("\nNice, you got a B!")
    elif grade > 69:
        print("\nNot bad, you got a C!")
    elif grade > 59:
        print("\nYou got a D. Start panicking.")
    else:
        print("\nYour failed. Sucks to be you.")

    run = input("Do you have any other grades? Y/N:")

