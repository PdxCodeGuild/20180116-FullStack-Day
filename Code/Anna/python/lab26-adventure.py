"""
Lab 26
(Space) adventure awaits!
-------------------------
Credits:
    pyaudio with threading code: https://gist.github.com/THeK3nger/3624478
    sound effects: http://www.audiomicro.com/free-science-fiction-sci-fi-sound-effects
    intro and outro music: http://soundimage.org/sci-fi/
    8-bit cantina song: https://www.youtube.com/watch?v=o8l8SuBj9-c
    ascii playing cards: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
    ascii art: http://www.chris.com/ascii/joan/www.geocities.com/SoHo/7373/transp.html#plane
    ascii text: http://patorjk.com/software/taag/
-------------------------
"""

from __future__ import print_function
import chalk
import random
from time import sleep
import pyaudio
import wave
import threading
# import pygame.examples.stars
#
# pygame.init()

# TODO: add pygame minigame?


class Game:
    """This defines the game mechanics and sets up the initial conditions"""

    def __init__(self, width=10, height=20):
        self.width = width  # the width of the board
        self.height = height  # the height of the board

    def __getitem__(self, j):
        return self.board[j]

    def make_board(self, diff_setting, astroids):
        """Create a board with the given width and height
        We'll use a list of lists to represent the board,
        and will add initial enemies to the board"""
        board = []  # start with an empty list
        for i in range(self.height):  # loop over the rows
            board.append([])  # append an empty row
            for j in range(self.width):  # loop over the columns
                board[i].append(chalk.blue('[    ]'))  # append an empty space to the board
        # add asteroids in random locations
        for i in range(astroids):
            ast_x = random.randint(0, self.height - 2)
            ast_y = random.randint(0, self.width - 2)
            board[ast_x][ast_y] = chalk.blue('[ ☄️ ]')
        # add enemies in random locations
        for i in range(diff_setting):
            enemy_x = random.randint(0, self.height - 2)
            enemy_y = random.randint(0, self.width - 2)
            board[enemy_x][enemy_y] = chalk.blue('[ 👾 ]')
        # add boss enemies in random locations
        for i in range(2):
            enemy_x = random.randint(0, self.height - 2)
            enemy_y = random.randint(0, self.width - 2)
            if board[enemy_x][enemy_y] != chalk.blue('[ 👾 ]'):  # otherwise there's aliens on top of aliens,
                board[enemy_x][enemy_y] = chalk.blue('[ 👽 ]')   # and nobody wants that
            else:
                board[enemy_x - 1][enemy_y] = chalk.blue('[ 👽 ]')
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
        if shield_level > 20:
            return chalk.yellow(f"Shields: {shield_level}%")
        else:
            return chalk.red(f"Shields: {shield_level}%")

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


class BonusWave(threading.Thread):
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
        f = wave.open(r"audio/cantina.wav", "rb")
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


def scary_space():
    print(chalk.yellow(
        "Trust me, you don't want to venture out into the vastness of space. It's scary out there..."))


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
    Space Code School students - and their particularly
    brutal bosses, 👽's.
    """))
    sleep(12)
    print(chalk.green("""
    As luck would have it, just your escape pod is
    equipped with a space laser gun. As soon as
    you clear the path of enemies, your classmates can 
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
    print(chalk.yellow('''


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
    s.sound_effect('audio/ending_theme_short.wav')
    print(chalk.yellow('''
                                         ...or is it?
    '''))
    sleep(2)
    print(chalk.green("\tWould you like to see the alternate ending? y/n"))
    ending = input("> ")
    if ending == 'y':
        alt()


def alt():
    # get the blackjack bonus game
    from Code.Anna.python import blackjack
    from blackjack import game
    from blackjack import comp_game

    # bonus game set-up
    sleep(2)
    print(chalk.yellow("""
    You and your classmates land safely on the warm yellow planet below.
    The streets are clear, and the only building in sight with any
    commotion is the Space Bar...
    """))
    b.start()   # please don't sue me, George Lucas...
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
    That price is beating her at Space Blackjack 🃏. Will you play? y/n
    """))
    choice = input("> ")
    if choice == 'y':
        winner = False
        while winner is False:

            bj_result = game()
            bj_ruler = comp_game()

            if bj_result == bj_ruler:
                print("It's a tie, play again!\n")

            elif bj_result > 21 and bj_ruler > 21:
                print("You both busted, play again!\n")

            elif bj_result <= 21 and bj_result > bj_ruler or bj_ruler > 21:
                print("You win!\n")
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
                s.sound_effect('audio/win.wav')
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
                s.sound_effect('audio/space_launch.wav')
                print(chalk.yellow("""
            You make it back to Space Code School, and after studying hard and
            graduating with flying colors, you get a job as the lead
            python developer on a new, top-secret, government project. 
            Something about a 'Star' of 'Death'...
                    """))
                sleep(5)
                outro()
                break
            else:
                print("You lose!\n")
                sleep(1)
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
                s.sound_effect('audio/space_cats.wav')
                outro()
                break
    else:
        outro()


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

    print("\nYou are surrounded by enemies! And asteroids, which can damage your shields!"
          "\nChoose 'u' for up, 'd' for down, 'r' for right, 'l' for left, or 'q' to quit."
          "\nIf you encounter an enemy, choose 'a' for attack or 'r' for 'run'."
          "\nType anything else at your own peril..."
          "\nAnd whatever you do, don't run out of gas!\n")
    round_one = True

    # loop until the user says 'done' or dies
    while True:
        print("What is your command?")
        command = input('> ')  # get the command from the user

        if command == 'q':
            break  # exit the game
        elif command == 'l':
            if player_y - 1 < 0:
                scary_space()
            else:
                player_y -= 1  # move left
        elif command == 'r':
            if player_y + 1 > play_game.width - 1:
                scary_space()
            else:
                player_y += 1  # move right
        elif command == 'u':
            if player_x - 1 < 0:
                scary_space()
            else:
                player_x -= 1  # move up
        elif command == 'd':
            if player_x + 1 > play_game.height - 1:
                scary_space()
            else:
                player_x += 1  # move down
        else:
            print("Invalid command.")

        # check if the player is on the same space as an asteroid
        if board[player_x][player_y] == chalk.blue('[ ☄️ ]'):
            print("You've hit an asteroid field! Shields damaged")
            s.sound_effect('audio/meteor.wav')
            shield_level -= 10

        # find emergency fuel if conditions met
        if fuel_level < 6 and num_enemies < 4:
            fuel_level += 10
            print(chalk.green("You found a spare gas canister ⛽ hidden in the escape pod!"
                             "\nNow let's get the rest of those aliens!"))

        # repopulate board with 4 additional enemies, but only the first time num_enemies drops to 2
        if num_enemies == 2 and round_one is True:
            print("Oh no, they're onto you! They've called for reinforcements!")
            sleep(1)
            for i in range(4):
                enemy_x = random.randint(0, play_game.height - 2)
                enemy_y = random.randint(0, play_game.width - 2)
                board[enemy_x][enemy_y] = chalk.blue('[ 👾 ]')
            num_enemies += 4
            round_one = False

        # check if the player is on the same space as an enemy
        if board[player_x][player_y] == chalk.blue('[ 👾 ]'):
            print('You\'ve encountered an alien enemy!')
            action = input('What will you do? ')
            if action == 'a':
                num_enemies -= 1
                s.sound_effect('audio/laser_gun_shot.wav')
                if num_enemies != 0:
                    print(f'You\'ve slain the enemy and stolen their fuel! Keep going, there are {num_enemies} enemies left.')
                    board[player_x][player_y] = chalk.blue('[    ]')  # remove the enemy from the board
                    fuel_level += 5
                sleep(2)
            elif action == 'r':
                s.sound_effect('audio/whoosh_by.wav')
                if num_enemies != 0:
                    print(
                        'You made a run for it, but took damage on your way!')
                    shield_level -= random.randint(0, 20)
                sleep(2)
            else:
                s.sound_effect('audio/laser_sounds_2.wav')
                print("You've been hit! Your shields have been damaged.")
                shield_level -= 50

        # check if the player is on the same space as a boss enemy
        if board[player_x][player_y] == chalk.blue('[ 👽 ]'):
            print('You\'ve encountered a boss enemy!')
            action = input('What will you do? ')
            if action == 'a':
                num_enemies -= 1
                s.sound_effect('audio/laser_gun_shot.wav')
                if num_enemies != 0:
                    print(
                        f'You\'ve slain the enemy and but took damage to your shields! Keep going, there are {num_enemies} enemies left.')
                    board[player_x][player_y] = chalk.blue('[    ]')  # remove the enemy from the board
                    shield_level -= 20
                    fuel_level += 10
                sleep(2)
            elif action == 'r':
                s.sound_effect('audio/whoosh_by.wav')
                if num_enemies != 0:
                    print(
                        'You made a run for it, but took damage on your way! '
                        '\nLuckily, the boss got bored and took off to do boss alien things.')
                    board[player_x][player_y] = chalk.blue('[    ]')  # remove the enemy from the board
                    num_enemies -= 1
                    shield_level -= random.randint(20, 50)
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
        if shield_level < 0:
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
                "With no shields left, your escape pod was blown to smithereens."
                "\nHopefully your classmates can make it without you..."))
            outro()
            break
        print()


# this is where we finally launch the game

s = WavePlayer()                                            # initialize intro music
b = BonusWave()                                             # initialize music for bonus game
intro()                                                     # start the intro to the game
diff_setting = difficulty_setting()                         # prompt the user for the difficulty setting
asteroids = int(diff_setting * 2)                           # num of asteroids based on diff setting
num_enemies = diff_setting + 2                              # add 2 to num enemies for 2 bosses

play_game = Game()                                          # initialize the game
player_i, player_j = play_game.player_position()            # set the initial player position
board = play_game.make_board(diff_setting, asteroids)       # set up the playing board

game_on(player_i, player_j, num_enemies)                    # start the Space Adventure Game!
