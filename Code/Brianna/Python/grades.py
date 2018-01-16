
number_grade = int(input("What is your number score?\n:"))


if number_grade >= 90:
    print("Congratulations! You got an A!")
elif number_grade >= 80:
    print("Doing good! You got a B!")
elif number_grade >= 70:
    print("Whew! Good job, you managed a C!")
elif number_grade >= 60:
    print("Oh! You were so close! Give it another go. You got a D.")
elif number_grade < 60:
    print("Ouch! Time to hit the books again. You got an F.")
else:
    print("I don't understand! @.@")