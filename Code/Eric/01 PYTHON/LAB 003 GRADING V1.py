test_score = input("\nWhat was your grade on the test?\n\n:")
test_score = float(test_score)

#A Range
if test_score >= 97.00:
    print("\nYou got an A+!")
elif test_score >= 94.00:
    print("\nYou got an A!")
elif test_score >= 90.00:
    print("\nYou got an A-!")

#B Range
elif test_score >= 87.00:
    print("\nYou got a B+!")
elif test_score >= 84.00:
    print("\nYou got a B!")
elif test_score >= 80.00:
    print("\nYou got a B-!")

#C Range
elif test_score >= 77.00:
    print("\nYou got a C+!")
elif test_score >= 74.00:
    print("\nYou got a C!")
elif test_score >= 70.00:
    print("\nYou got a C-!")

#D Range
elif test_score >= 67.00:
    print("\nYou got a D+!")
elif test_score >= 64.00:
    print("\nYou got a D!")
elif test_score >= 60.00:
    print("\nYou got a D-!")

#Fail
elif 0 <= test_score <= 59.99:
    print("\nYou got an F!\nand failed! =(")
