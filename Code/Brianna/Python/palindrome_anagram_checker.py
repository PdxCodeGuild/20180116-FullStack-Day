def check_palendrome(a_string):
    if word[:] == word[::-1]:
        print("This is a palendrome.")
    else:
        print("This is not a palendrome.")

word = input("Type in a word to check and see if it's a palendrome.\n:")

check_palendrome(word)

