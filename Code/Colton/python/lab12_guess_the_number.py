import random
computer = random.randint(1, 10)
user = int(input("Guess a number between 1 and 10.\n:"))
print(computer)
count = 0
if user == computer:
    pass
while user != computer and count < 10:
    if user < computer:
        user = int(input("Too low.Guess again.\n:"))
        count += 1
    if user > computer:
        user = int(input("Too high.Guess again.\n:"))
        count += 1
    print(f'''You have guessed {count} times.''')
if count >= 10:
    print("No more guesses")
else:
    print("You got it.")




