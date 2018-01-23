"""
Lab 3
Let's get grading!
"""

run = "Y"

while run == "Y":
    grade = int(input("What grade did you get? "))
    if grade % 10 > 6:
        plus = "+"
    elif grade % 10 < 4:
        plus = "-"
    else:
        plus = ""

    if grade > 100:
        print("\nYou overachiever, you!")
    elif grade == 100:
        print("\nPerfect score, look at you!")
    elif grade > 89:
        print(f"\nSweet, you got an A{plus}!")
    elif grade > 79:
        print(f"\nNice, you got a B{plus}!")
    elif grade > 69:
        print(f"\nNot bad, you got a C{plus}!")
    elif grade > 59:
        print(f"\nYou got a D{plus}. Start panicking.")
    else:
        print("\nYour failed. Sucks to be you.")

    run = input("Do you have any other grades? Y/N: ")

