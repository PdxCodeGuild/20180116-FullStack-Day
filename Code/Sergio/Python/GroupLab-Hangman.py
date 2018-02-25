import random

with open('../../1 Python/data/english.txt', 'r') as f:
    lines = f.read().split('\n')

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
./ \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
./ \. |
      |
=========''']

print(hangman_pics[0])

def get_word():
    while True:
        word = random.choice(lines)
        if len(word) > 5:
            return word

def play():

    secret_word = list(get_word())
    print(secret_word)
    blank_word = list('_' * len(secret_word))
    print(blank_word)
    letters_guessed = []
    guesses_remaining = 10
    hangman_index = 0

    while blank_word != secret_word and guesses_remaining > 0:
        correct = False
        guess = input('Guess a letter: ')

        for i, char in enumerate(secret_word):
            if secret_word[i] == guess:
                blank_word[i] = guess
                print(f"Yes, {guess} is in the word!")
                correct = True

        if not correct and guess not in letters_guessed:
            guesses_remaining -= 1
            hangman_index += 1
            letters_guessed.append(guess)
            print(f'No, {guess} is not the word.')
            print(f"You have guessed the letter: {', '.join(letters_guessed)}")
            print(f"You have {guesses_remaining} guesses remaining.")
            print(hangman_pics[hangman_index])

        elif not correct:
            print('You already guessed that letter.')
            print(hangman_pics[hangman_index])
            print(f"You have {guesses_remaining} guesses remaining.")
        print(blank_word)

    if guesses_remaining == 0:
        print('Game over')
    else:
        print(f"\nYes, the word is '{''.join(secret_word)}'") #joins list
play()
