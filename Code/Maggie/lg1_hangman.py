import random


with open('../../1 Python/data/english.txt', 'r') as f:
    lines = f.read().split('\n')


def get_word():
    while True:
        word = random.choice(lines)
        if len(word) > 5:
            return word


hangman = hangman_pics = ['''
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


def play():
    guesses_remaining = 10
    secret_word = list(get_word())
    blank_word = list('_' * len(secret_word))
    letters_guessed = []
    hangman_ind = 0
    print('Let\'s play hangman! Try to guess the word within 10 tries.')
    while blank_word != secret_word and guesses_remaining > 0:
        correct = False
        # print(secret_word)  #for debugging
        print(' '.join(blank_word))
        guess = input('guess a letter: ')
        print(f'you\'ve guessed {guess}.')
        for i, char in enumerate(secret_word):
            if char == guess:
                print(f'Correct! {guess} is in the word.')
                blank_word[i] = guess
                correct = True
        if not correct and guess not in letters_guessed:
            print('Incorrect!')
            letters_guessed.append(guess)
            guesses_remaining -= 1
            hangman_ind += 1
        elif guess in letters_guessed:
            print('You\'ve already guessed that letter. Try again!')
        print(f'{guesses_remaining} guesses remain.\n{hangman_pics[hangman_ind]}')
        print(f'Incorrect letters_guessed: {", ".join(letters_guessed)}')
    print(' '.join(blank_word))
    if guesses_remaining == 0:
        print(f'Sorry, No more guesses remain. You\'ve lost the game. \nThe word was {"".join(secret_word)}')
    else:
        print('You got it!')


play()
