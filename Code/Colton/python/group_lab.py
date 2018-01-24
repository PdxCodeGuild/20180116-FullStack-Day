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
used_letters = []
guess_letters = ('_' * len(word))
guess_letters = list(guess_letters)

while user_guess < 5:
    user_input = input("Guess a letter.\n:")
    used_letters.append(user_input)
    print(f'You have guessed {used_letters}.')
    for i in range(len(word)):
        if user_input == word[i]:
            guess_letters[i] = user_input
            if ''.join(guess_letters) == ''.join(word):
                print("You win!!!!")
                user_guess = 1000


    if user_input not in word:
        user_guess += 1
    print(' '.join(guess_letters))
word = ''.join(word)
if ''.join(guess_letters) != ''.join(word):
    print("Ow! You didn't get it!")
    print(f'The word was {word}.')






#user_guess = 0
#while user_guess < 11:
#    print('-' * len(word))
#
#    guess_letter = input("Guess a letter\n:")
