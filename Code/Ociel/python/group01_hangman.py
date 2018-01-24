

import random

def get_word():
    valid_word_list = []
    with open('english.txt', 'r') as word_file:
        for line in word_file:
            if len(line.strip()) > 5:
                valid_word_list.append(line.strip())
    return random.choice(valid_word_list)

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
=========''']


play = True


while play:
    pic = 0
    word = get_word()
    win = False
    already_used = []
    solution = ['_'] * len(word)
    game_over = False
    while not game_over:
        print(hangman_pics[pic])
        print(f'Bad guesses remaining {6-pic}:')
        print(' '.join(solution))
        print("Letters used: ", ','.join(already_used))
        guess = input('Enter a letter: ').lower()
        while guess in already_used:
            guess = input('You already used that letter, guess again.')
        already_used.append(guess)
        for i in range(len(word)):
            if guess == word[i]:
                solution[i] = guess
        if ''.join(solution) == word:
            win = True
            game_over = True
            break
        if guess not in word:
            pic += 1
        if pic == 6:
            game_over = True
            break

    if win:
        print(word)
        print('Good Job Buddy!')
    else:
        print(hangman_pics[pic])
        print(word)
        print('You die!')

    if input('Enter \'q\' to quit, any other key to play again') == 'q':
        play = False
        print('Goodbye')