
number_grade = int(input("What is your number score?\n:"))


plus_minus = number_grade % 10

if plus_minus >= 7:
    plus_minus = "+"
elif plus_minus <= 3:
    plus_minus = "-"
else:
    plus_minus = ""


if number_grade >= 90:
    print("Congratulations! You got an A" + plus_minus + "!")
elif number_grade >= 80:
    print("Doing good! You got a B" + plus_minus + "!")
elif number_grade >= 70:
    print("Whew! Good job, you managed a C" + plus_minus + "!")
elif number_grade >= 60:
    print("Oh! You were so close! Give it another go. You got a D" + plus_minus + ".")
elif number_grade < 60:
    print("Ouch! Time to hit the books again. You got an F.")
else:
    print("I don't understand! @.@")

