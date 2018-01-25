
"""
Hangman game
"""

import random


def load():
    with open('english.txt', 'r') as f:
        contents = f.read().lower()
    words = contents.split('\n')
    list_words = []
    for word in words:
        if len(word) > 4 and len(word) < 12:
            list_words.append(word)
    return list_words

list_words = load()

# pick a word
chosen_word = random.choice(list_words)

unknown_word = []
guesses_remaining = 10
for letter in chosen_word:
    unknown_word.append('_')

already_guessed = []
while guesses_remaining > 0:
    print(' '.join(unknown_word))
    print('# of guesses remaining:', guesses_remaining)
    print('already guessed: '+', '.join(already_guessed))
    guess = input('Guess a letter: ')
    if guess in already_guessed:
        print('You\'ve already guessed that')
        continue
    already_guessed.append(guess)
    # if guess not in chosen_word:
    #    guesses_remaining -= 1
    found_letter = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            unknown_word[i] = chosen_word[i]
            found_letter = True
    if not found_letter:
        guesses_remaining -= 1
    if '_' not in unknown_word:
        print('You\'ve won!')
        break

# and list of letters already guessed
print(chosen_word)
