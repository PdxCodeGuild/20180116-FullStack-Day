again = "yes"
while again == 'yes':
    my_grade = int(input("What grade did you recieve?\n:"))
    if my_grade <59:
        print("You failed")
    elif my_grade >=60 and my_grade <=63:
        print("You got a D-.")
    elif my_grade >=64 and my_grade <=66:
        print("You got a D-.")
    elif my_grade >=67 and my_grade <=69:
        print("You got a D+.")
    elif my_grade >=70 and my_grade <=73:
        print("You got a C-.")
    elif my_grade >=74 and my_grade <=76:
        print("You got a C.")
    elif my_grade >=77 and my_grade <=79:
        print("You got a C+.")
    elif my_grade >=80 and my_grade <=83:
        print("You got a B-.")
    elif my_grade >=84 and my_grade <=86:
        print("You got a B.")
    elif my_grade >=87 and my_grade <=89:
        print("You got a B+.")
    elif my_grade >=90 and my_grade <=93:
        print("You got an A-")
    elif my_grade >=94 and my_grade <=96:
        print("You got an A")
    elif my_grade >=96 and my_grade <=100:
        print("Congratulations, you got an A+")
    again = input("Want to put in another grade? Yes or No\n:").lower()

