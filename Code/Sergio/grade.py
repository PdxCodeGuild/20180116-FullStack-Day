get_grade = input('Grade yourself! Enter a number between 0 and 100\n:')
if int(get_grade) >= 90:
    print("You got an A!")
elif int(get_grade) >= 80:
    print("You got a B..")
elif int(get_grade) >= 70:
    print("You got a C........")
elif int(get_grade)  >= 60:
    print("You got a D :(")
elif int(get_grade)  >= 0:
    print("You got a F LOL")
elif int(get_grade)  < 0:
    print("Negative")
