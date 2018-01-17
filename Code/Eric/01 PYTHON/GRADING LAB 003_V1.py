test_score = float(input("\nWhat was your grade on the test?\n\n:"))
test_score = float(test_score)

#A Range
if test_score >= 97.00 and test_score <= 100.00:
    print("\nYou got an A+!")
elif test_score >= 94.00 and test_score <= 96.99:
    print("\nYou got an A!")
elif test_score >= 90.00 and test_score <= 93.99:
    print("\nYou got an A-!")

#B Range
if test_score >= 87.00 and test_score <= 89.99:
    print("\nYou got a B+!")
elif test_score >= 84.00 and test_score <= 86.99:
    print("\nYou got a B!")
elif test_score >= 80.00 and test_score <= 83.99:
    print("\nYou got a B-!")

#C Range
if test_score >= 77.00 and test_score <= 79.99:
    print("\nYou got a C+!")
elif test_score >= 74.00 and test_score <= 76.99:
    print("\nYou got a C!")
elif test_score >= 70.00 and test_score <= 73.99:
    print("\nYou got a C-!")

#D Range
if test_score >= 67.00 and test_score <= 69.99:
    print("\nYou got a D+!")
elif test_score >= 64.00 and test_score <= 66.99:
    print("\nYou got a D!")
elif test_score >= 60.00 and test_score <= 63.99:
    print("\nYou got a D-!")

#Fail
elif test_score >= 0 and test_score <= 59.99:
    print("\nYou got an F!\nand failed! =(")