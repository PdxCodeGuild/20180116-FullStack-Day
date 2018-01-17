test_score = int(input("\nWhat was your grade on the test?\n\n:"))

if test_score >= 90 and test_score <= 100:
    print("\nYou got an A!")
elif test_score >= 80 and test_score <= 89:
    print("\nYou got a B!")
elif test_score >= 70 and test_score <= 79:
    print("\nYou got a C!")
elif test_score >= 60 and test_score <= 69:
    print("\nYou got a D!")
elif test_score >= 0 and test_score <= 59:
    print("\nYou got an F!")