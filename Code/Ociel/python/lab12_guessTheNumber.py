import random

# Version 1

machineGuess = random.randint(1,10)
tries = 0
userGuess = 0

while userGuess != machineGuess:
    userGuess = int(input("Guess the number: "))
    if userGuess != machineGuess:
        print('Try again!')
    tries += 1

print(f"Correct you guessed in {tries} times")

# # Version 2

# machineGuess = random.randint(1,10)
# tries = 0
# userGuess = 0
#
# while True:
#     userGuess = int(input("Guess the number: "))
#     if userGuess != machineGuess:
#         print('Try again!')
#     tries += 1
#     if userGuess == machineGuess:
#         break
#
# print(f"Correct you guessed in {tries} times")


# # Version 3
#
# machineGuess = random.randint(1,10)
# tries = 0
# userGuess = 0
# lastGuess = 0
#
# while True:
#     userGuess = int(input('Guess the number: '))
#     if userGuess != machineGuess:
#         print('Try Again!')
#         lastGuess = userGuess
#     if lastGuess > machineGuess:
#         print('Too High!')
#     if lastGuess < machineGuess:
#         print('Too Low!')
#     if machineGuess == userGuess:
#         break
#     tries += 1
#
# print(f"Correct you guessed in {tries} times")

# # Version 5
# # THe computer turn to
# tries = 0
# lastGuess = 0
# userGuess = int(input('Guess the number: '))
#
# while True:
#     machineGuess = random.randint(1, 10)
#     if machineGuess == userGuess:
#         break
#     tries += 1
#
# print(f"Correct you guessed in {tries} times")
