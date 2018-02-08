from __future__ import print_function
import chalk
from time import sleep
from audio_classes import *


def intro():
    s.start()       # for some reason, this has to be s.start() and not s.run(), which won't work
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
    # get the blackjack bonus minigame
    from space_adventure.blackjack import game, comp_game

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

            elif 21 >= bj_result > bj_ruler or bj_ruler > 21:
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
            Python developer on a new, top-secret, government project. 
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
                # get the Herding Space Cats bonus minigame
                from space_adventure.adventure_minigame import main
                cats = main()
                outro()
                break
    else:
        outro()


s = WavePlayer()                                            # initialize intro music
b = BonusWave()                                             # initialize music for bonus game
