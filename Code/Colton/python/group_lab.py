import random
with open('english.txt', 'r') as f:
    lines = f.read().split('\n')
    word = random.choice(lines)
    while len(word) < 5:
        continue
    print(word)

word = list(word)
#------------------------------------
user_guess = 0
while user_guess < 11:
    user_input = input("Guess a letter.\n:")
    used_letters = []

    for i in range(len(word)):
        if user_input == word[i]:
            guess_letters[i] = user_input


guess_letters = ('_ ' * len(word))



guess_letters = list(guess_letters)


#user_guess = 0
#while user_guess < 11:
#    print('-' * len(word))
#
#    guess_letter = input("Guess a letter\n:")
