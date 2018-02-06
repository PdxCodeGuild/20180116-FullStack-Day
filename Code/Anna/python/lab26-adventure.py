"""
Lab 26
(Space) adventure awaits!
"""

from __future__ import print_function
import chalk
import random
from time import sleep
import pyaudio
import wave
import threading
import pygame.examples.stars

from Code.Anna.python import blackjack

pygame.init()

# TODO: add bomb option to clear board (have to go get bomb first though) (if bomb, clear enemies)
# TODO: random asteroids! If you hit one, your shields go down 10%


class Game:
    """This defines the game mechanics and sets up the initial conditions"""

    def __init__(self, width=10, height=20):
        self.width = width  # the width of the board
        self.height = height  # the height of the board

    def __getitem__(self, j):
        return self.board[j]

    def make_board(self, diff_setting):
        """Create a board with the given width and height
        We'll use a list of lists to represent the board,
        and will add initial enemies to the board"""
        board = []  # start with an empty list
        for i in range(self.height):  # loop over the rows
            board.append([])  # append an empty row
            for j in range(self.width):  # loop over the columns
                board[i].append(chalk.blue('[    ]'))  # append an empty space to the board
        # add enemies in random locations
        for i in range(diff_setting):
            enemy_x = random.randint(0, self.height - 2)
            enemy_y = random.randint(0, self.width - 2)
            board[enemy_x][enemy_y] = chalk.blue('[ 👾 ]')
        return board

    def fuel_gage(self, fuel_level):
        if fuel_level > 18:
            return chalk.green(f"Fuel level: {'*' * fuel_level}")
        elif fuel_level > 9:
            return chalk.yellow(f"Fuel level: {'*' * fuel_level}")
        elif fuel_level > 0:
            return chalk.red(f"Fuel level: {'*' * fuel_level}")
        else:
            s.sound_effect('audio/atomic_overload.wav')
            print(chalk.red("You're out of gas! Hopefully your classmates can make it without you..."))
            outro()

    def shields(self, shield_level):
        if shield_level == 100:
            return chalk.green(f"Shields: {shield_level}%")
        else:
            return chalk.yellow(f"Shields: {shield_level}%")

    def player_position(self):
        """Starting position in the middle of the board"""
        player_x = 10
        player_y = 4
        return player_x, player_y


class WavePlayer(threading.Thread):
    """
    A simple class based on PyAudio to play a sine wave.
    It's a threading class. You can play audio while your application
    continues to do stuff.
    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.p = pyaudio.PyAudio()

        self.fs = 44100          # sampling rate, Hz, must be integer

    def run(self):
        """
        Just another name for self.start()
        """
        # define stream chunk
        chunk = 1024

        # open a wav format music
        f = wave.open(r"audio/beginning_theme.wav", "rb")
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

        # stop audio stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()

    def sound_effect(self, path):
        """
        Use for sound effects throughout the game
        """
        # define stream chunk
        chunk = 1024

        # open a wav format music
        f = wave.open(path, "rb")
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

        # stop audio stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()


def difficulty_setting():
    print("\nWhat is your difficulty setting? Choose 'normal', 'hard', or 'hardcore'. (There is no 'easy' in space)")
    difficulty = input("> ")
    if difficulty == 'hardcore':
        diff_setting = 10
    elif difficulty == 'hard':
        diff_setting = 6
    else:
        diff_setting = 4
    return diff_setting


def intro():
    s.start()
    sleep(1)
    print(chalk.green("\n\t\t\t\t\t\t\t\tWelcome to the..."))
    sleep(1)
    print(chalk.green(r"""
                   
                       ███████╗██████╗  █████╗  ██████╗███████╗
                       ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝
                       ███████╗██████╔╝███████║██║     █████╗  
                       ╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝  
                       ███████║██║     ██║  ██║╚██████╗███████╗
                       ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
    """))
    sleep(1)
    print(chalk.green(r'''
     █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
    ██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
    ███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  
    ██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  
    ██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗
    ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
    '''))
    sleep(1)
    print(chalk.green(r'''
                           ██████╗  █████╗ ███╗   ███╗███████╗™
                          ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                          ██║  ███╗███████║██╔████╔██║█████╗  
                          ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                          ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                           ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                             
        '''))
    sleep(3)
    print(chalk.green("""
    Not too long ago in the galaxy next door,
    your spaceship ran out of space-gas as you were 
    on the way to Space Code School with some of
    your classmates.
    """))
    sleep(7)
    print(chalk.blue(r"""                           *
               *   |||      |||         .
         *         | |  __  | |   *               *
    |-|_____-----/   |_|  |_|   \-----_____|-|
    |_|_________{   }|  (^) |{  }__________|_|  
     ||          |_| |   ^  | |_|          ||  
     |              \|  /\  |/              |  
     |         *     \ |--| /               |    .
     =               \ |__| /         *     =    
     +               \      /               +
              .       \    /    
        *             \    /    *
                       \  /                      *
 .                     \  /                             .
             .         \  /      .
                       \  /
                       \  /              *
      *                \  /
                        \/             .              .
             .     *            *      
                                                *                
    """))
    sleep(2)
    print(chalk.green("""
    Now you find yourself stranded in a strange
    corner of the universe, with little hope for
    rescue. With the last bit of fuel, you light
    up your radar to see what's out there...
    """))
    sleep(7)
    s.sound_effect('audio/satellite_noise.wav')
    print(chalk.green("\tA planet, and within range!"))
    print(chalk.yellow(r"""
            ~+
    
                     *       +
               '                  |
           ()    .-.,="``"=.    - o -
                 '=/_       \     |
              *   |  '=._    |
                   \     `=./`,        '
                .   '=.__.=' `='      *
       +                         +
            O      *        '       .
            
    """))
    sleep(2)
    print(chalk.green("""
    Luckily, your ship is equipped with just enough
    escape pods for everyone, and they all still
    have a full tank. The nearby planet is
    inhabited by friendly traders who could 
    offer help. You all just have to make it there
    without getting eaten by 👾's - a hostile 
    alien race with a particular fondness for eating
    Space Code School students.
    """))
    sleep(12)
    print(chalk.green("""
    As luck would have it, just your escape pod is
    equipped with a space laser gun. As soon as
    you clear the path of 👾's, your classmates can 
    follow to safety. Will you save the day?
    """))
    sleep(7)
    print(chalk.green("""
    You each enter your escape pod and are on your 
    way through the darkness of space...
    """))
    sleep(7)
    print(chalk.blue(r"""
           *        | | | | |         *
      *               | | |    *           .      *
                        |
       .      *                          *
                    .-;;;;;-.
                  .;;;;;;;;;;;.    .
  .      *       /;;;' o o ';;;\                 .
                ;;;; o /^\ o ;;;;           *
        .       ;;;; o \_/ o ;;;;
  *              \;;;. o o .;;;/        .
      .           ';;;;;;;;;;;'     *
                    '-;;;;;-'
              *                                  *
    """))
    s.sound_effect('audio/space_launch.wav')
    print(chalk.green("\n\tGood luck!"))
    sleep(5)


def outro():
    sleep(2)
    print(chalk.green('''


                 ██████╗  █████╗ ███╗   ███╗███████╗
                ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                ██║  ███╗███████║██╔████╔██║█████╗  
                ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                  ██████╗ ██╗   ██╗███████╗██████╗ 
                 ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                 ██║   ██║██║   ██║█████╗  ██████╔╝
                 ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                 ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                  ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝

    '''))
    s.sound_effect('audio/ending_theme.wav')
    print(chalk.green("\tThanks for playing!"))
    # pygame.examples.stars.main()


def outro_alt():
    sleep(2)
    print(chalk.green('''


                 ██████╗  █████╗ ███╗   ███╗███████╗
                ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                ██║  ███╗███████║██╔████╔██║█████╗  
                ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                  ██████╗ ██╗   ██╗███████╗██████╗ 
                 ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                 ██║   ██║██║   ██║█████╗  ██████╔╝
                 ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                 ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                  ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝

    '''))
    s.sound_effect('audio/ending_theme.wav')
    print(chalk.green("\tWould you like to see the alternate ending? y/n"))
    ending = input("> ")
    if ending == 'y':
        alt()


def alt():
    sleep(2)
    print(chalk.yellow("""
    You and your classmates land safely on the warm yellow planet below.
    The streets are clear, and the only building in sight with any
    commotion is the Space Bar...
    """))
    sleep(5)
    print(chalk.yellow("""

     .     .               . :
     !          _______ +_______
     |         /  _____)/  ___  \  +
- --(+)--- -  /  /_____/  /___)  \    :     ,------.
     T       (______   )   _______)     .   |       \\
     !   :.________/  /\  \_________________|______  \\
     :     [_(_______/__\__)______________________]___\\
 |         |                         | SPACE BAR  ]|[
-+--    :  |  ,--.    ,--.    ,--.    `''''''''''''|`---.
 !    +    | ((_  )  ((_  )  ((_  )  / 0-----0 \  |[__\\\\`._______________________
           |  `--'    `--'    `--'  /  |     |  \ | _____ _  _            |-|  /'
           |                        \  |     |  / |(O==o  _,--------------'-'-'
           |             ,-"-.       \ 0-----0 /  | `---,
           |____________( |`- )______________________|____/
  +                .     `-.-'     .        |    |____/ 
        .             .    |     .       :  |________/
           +    o!O      __I__+
   .:                   (  I  )    +
                         \___/

    """))
    sleep(2)
    print(chalk.yellow("""
    Inside, you find the planet's ruler, and she's willing to give you enough
    fuel to get you to Space Code School... for a price.
    """))
    sleep(5)
    print(chalk.yellow("""
    _____________________
   |         |_________
   |        [___________
   |          |   |   |
   |    @@   /_\ /_\ /_\\
   |   @()@
   |   _/\_
   | <&,)(V)-,_ ________
   |  ~_) ( [_________ _
   |  (_( _) |          |
   |   \ \~  |          |
   |    \,\, |          |
   |    /'/'o===========|
   |_,__-'-_,+-----------

    """))
    print(chalk.yellow("""
    That price is beating her at Space Blackjack 🃏. Will you play?
    """))
    choice = input("> ")
    if choice == 'y':
        from blackjack import game
        bj_result = game()
        bj_ruler = random.randint(10, 21)

        print(f"The ruler has 🃏 {bj_ruler}")

        if bj_result <= 21 and bj_result > bj_ruler:
            print("You win!")
            sleep(2)
            print(chalk.yellow("""
        Congrats, you've earned your fuel, and a tall frosty space beer!
    
                                 _, . '__ . 
                          '_(_0o),(__)o().
                        ,o(__),_)o(_)O,(__)o
                      o(_,-o(_ )(),(__(_)oO)_
                      .O(__)o,__).(_ )o(_)Oo_)
                       o/'"`\/'"`\/'"`\/'"\O_)0 
                       |    ||   ||   ||   |,_) 
                       |\___/\___/\___/\___|o(_)
                  .----|"\/'"`\/'"`\/'"`\/'|_/`)
                 /  .--| ||   ||   ||   || |O_) 
                |  /   |_/\___/\___/\___/\_|
                |  |   |/'"`\/'"`\/'"`\/'"`|
                |  |   |    ||   ||   ||   |
                |  |   |\___/\___/\___/\___|
                |  \   |"\/'"`\/'"`\/'"`\/"|
                 \  '--| ||   ||   ||   || |
                  '----|_/\___/\___/\___/\_|
                       |/'"`\/'"`\/'"`\/'"`|
                       |    ||   ||   ||   |
                        \___/\___/\___/\__/
                       `""""""""""""""""""

                """))
            outro()
        else:
            print("You lose!")
            print(chalk.yellow("""
        Sadly, you never make it off the planet, have to drop out of
        Space Code School, and spend the rest of your life
        herding space cats.
         .                       .
    .                 _                 *              .
        *             \`"-.
                .      )  _`-.    .                        .
                      ,  : `. \\              *
             .        : _   '  \\
    *                 ; *` _.   `--._    .            .  
                      `-.-'          `-.
               .        |       `       `.                  *
       .                :.       .        \\   *          
                        | \  .   :   .-'   .
    *                   :  )-.;  ;  /      :       .
                *       :  ;  | :  :       ;-.           *
         .              ; /   : |`-:     _ `- )
      .              ,-' /  ,-' ; .-`- .' `--'   .            .
             *       `--'   `---' `---'            .

        (Hey, it could be worse)
                """))
            outro()
    else:
        return None


def game_on(player_x, player_y, num_enemies):
    # print out the initial board
    for i in range(play_game.height):
        for j in range(play_game.width):
            # if we're at the player location, print the player icon
            if i == player_x and j == player_y:
                print(chalk.blue('[ 🚀 ]'), end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
    # print the fuel gage
    fuel_level = 20  # initialize fuel
    print(play_game.fuel_gage(fuel_level))
    # print the shield level
    shield_level = 100  # initialize shields
    print(play_game.shields(shield_level))
    print()

    print("\nYou are surrounded by enemies! Choose 'u' for up, 'd' for down, 'r' for right, 'l' for left, or 'q' to quit. Just don't run out of gas...\n")
    round_one = True

    # loop until the user says 'done' or dies
    while True:
        print("What is your command?")
        command = input('> ')  # get the command from the user

        if command == 'q':
            break  # exit the game
        elif command == 'l':
            if player_y - 1 < 0:
                print(chalk.yellow(
                    "Trust me, you don't want to venture out into the vastness of space. It's scary out there..."))
            else:
                player_y -= 1  # move left
        elif command == 'r':
            if player_y + 1 > play_game.width - 1:
                print(chalk.yellow(
                    "Trust me, you don't want to venture out into the vastness of space. It's scary out there..."))
            else:
                player_y += 1  # move right
        elif command == 'u':
            if player_x - 1 < 0:
                print(chalk.yellow(
                    "Trust me, you don't want to venture out into the vastness of space. It's scary out there..."))
            else:
                player_x -= 1  # move up
        elif command == 'd':
            if player_x + 1 > play_game.height - 1:
                print(chalk.yellow(
                    "Trust me, you don't want to venture out into the vastness of space. It's scary out there..."))
            else:
                player_x += 1  # move down
        else:
            print("Invalid command.")

        # check if the player is on the same space as an enemy
        if board[player_x][player_y] == chalk.blue('[ 👾 ]'):
            print('You\'ve encountered an alien enemy!')
            action = input('What will you do? ')
            if action == 'attack':
                num_enemies -= 1
                s.sound_effect('audio/laser_gun_shot.wav')
                if num_enemies == 2 and round_one is True:
                    print("Oh no, they're onto you! They've called for reinforcements!")
                    sleep(1)
                    board[player_x][player_y] = chalk.blue('[    ]')  # remove the enemy from the board
                    for i in range(4):
                        enemy_x = random.randint(0, play_game.height - 1)
                        enemy_y = random.randint(0, play_game.width - 1)
                        board[enemy_x][enemy_y] = chalk.blue('[ 👾 ]')
                    num_enemies = 6
                    round_one = False
                if num_enemies != 0:
                    print(f'You\'ve slain the enemy and stolen their fuel! Keep going, there are {num_enemies} enemies left.')
                    board[player_x][player_y] = chalk.blue('[    ]')  # remove the enemy from the board
                    fuel_level += 5
                sleep(2)
            else:
                s.sound_effect('audio/laser_sounds_2.wav')
                print("You've been hit! Your shields have been damaged.")
                shield_level -= 50

        if num_enemies == 0:
            print("You did it! Your classmates can now land safely on the planet below!")
            s.sound_effect('audio/space_landing.wav')
            print(chalk.yellow('''
                                .                                            .
             *   .                  .              .        .   *          .
          .         .                     .       .           .      .        .
                o                             .                   .
                 .              .                  .           .
                  0     .
                         .          .                 ,                ,    ,
         .          \          .                         .
              .      \   ,
           .          o     .                 .                   .            .
             .         \                 ,             .                .
                    .-;;;;;-.
                  .;;;;;;;;;;;.    .
  .      *       /;;;' o o ';;;\                 .
                ;;;; o /^\ o ;;;;           *
        .       ;;;; o \_/ o ;;;;
  *              \;;;. o o .;;;/        .
      .           ';;;;;;;;;;;'     *
                    '-;;;;;-'  .                    .             .          ,
                              \          .                         .
        ____^/\___^--____/\____O______________/\/\---/\___________---______________
           /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
                 --           -            --  -      -         ---  __       ^
           --  __                      ___--  ^  ^                         --  __
    
                '''))
            sleep(2)
            outro_alt()
            break

        # print out the board
        for i in range(play_game.height):
            for j in range(play_game.width):
                # if we're at the player location, print the player icon
                if i == player_x and j == player_y:
                    print(chalk.blue('[ 🚀 ]'), end=' ')
                else:
                    print(board[i][j], end=' ')  # otherwise print the board square
            print()
        fuel_level -= 1
        print(play_game.fuel_gage(fuel_level))
        print(play_game.shields(shield_level))
        if fuel_level == 0:
            break
        if shield_level == 0:
            s.sound_effect('audio/space_noise.wav')
            # print out the board without the player, since the player was blown up #sadface
            for i in range(play_game.height):
                for j in range(play_game.width):
                    # if we're at the player location, print the player icon
                    if i == player_x and j == player_y:
                        print(chalk.blue('[    ]'), end=' ')
                    else:
                        print(board[i][j], end=' ')  # otherwise print the board square
                print()
            print(chalk.red(
                "With no shields left, your escape pod was blown to smithereens. Hopefully your classmates can make it without you..."))
            outro()
            break
        print()


s = WavePlayer()
intro()
diff_setting = difficulty_setting()
num_enemies = diff_setting

play_game = Game()
player_i, player_j = play_game.player_position()
board = play_game.make_board(diff_setting)

game_on(player_i, player_j, num_enemies)
