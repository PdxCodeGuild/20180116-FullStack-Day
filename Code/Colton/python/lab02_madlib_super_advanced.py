import random
print("Welcome to the maddest of Mad Libs")
answer = "yes"
while answer == "yes":
    loc = input("Give me 3 locations\n:")
    loc2 = loc.split(",")
    verb = input("Give me 3 verbs\n:")
    verb2 = verb.split(",")
    num = input("Give me a 3 numbers\n:")
    num2 = num.split(",")
    pet = input("What is your favorite animal?\n:")
    food = input("What is your favorite food?\n:")
    print("Great! Let's see what we have.")
    print("Now seeking " + pet + " in the " + random.choice(loc2) + " area. Needed for " + random.choice(verb2) + " training. Will pay in " + food + " or $" + random.choice(num2))
    answer = input("Try again? Yes or No?\n:").lower()


