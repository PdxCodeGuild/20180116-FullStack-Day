import random
print("Welcome to 8 Ball")
c = ["Yes", "No", "Maybe"]
answer = ("yes").lower()
while answer == ("yes"):
    input("Please type your question below.\n:")
    print(random.choice(c))
    answer = input("Try again? Yes or No\n:").lower()
    if answer == ("no"):
        break
    else:
        print("Let's try that again")
        answer = ("yes")
