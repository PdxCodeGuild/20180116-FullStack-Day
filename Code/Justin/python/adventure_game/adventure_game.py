"""Adventure Game!!!"""

import random
import itertools
import chalk





class Character():

    def __init__(self, kind, visible, health, weapon, location):
        self.kind = kind
        self.visible = visible
        self.location = location
        self.health = float(health)
        self.weapon = weapon

    def get_kind(self):
        return self.kind

    def get_visible(self):
        return self.visible

    def get_location(self):
        return self.location

    def get_health(self):
        return self.health

    def get_weapon(self):
        return self.weapon

    def update_location(self, location):
        self.location = location

    def update_health(self, value):
        self.health += value

    def update_weapon(self, weapon):
        self.weapon = weapon

    def update_visible(self, visible):
        self.visible = visible


class Thing():

    def __init__(self, kind, visible, location):
        self.kind = kind
        self.visible = visible
        self.location = location

    def get_kind(self):
        return self.kind

    def get_visible(self):
        return self.visible

    def get_location(self):
        return self.location

    def update_visible(self, visible):
        self.visible = visible




def make_board_string(board):
    # Update visibilty
    hero_r = hero.get_location()[0]
    hero_c = hero.get_location()[1]
    for r in range(1, rows + 1):
        for c in range(1, columns + 1):
            if board[(r, c)] in [None, hero]:
                continue
            if abs(hero_r - r) <= 3 and abs(hero_c - c) <= 3:
                board[(r, c)].update_visible(True)
            else:
                board[(r, c)].update_visible(False)
    if found_map:
        treasure.update_visible(True)


    # Construct string
    board_string = ''
    for r in range(1, rows + 1):
        board_string = board_string + '-' + ('----' * columns) + '\n'
        for c in range(1, columns + 1):
            if board[(r, c)] == None or board[(r, c)].get_visible() == False:
                icon = ' '
            else:
                icon = icon_dictionary[board[(r, c)].get_kind()]
            board_string = board_string + '| ' + icon + ' '
        board_string = board_string + '|\n'
    board_string = board_string + '-' + ('----' * columns)
    return board_string

def generate_filename(name):
    return name + '.txt'

def print_image(file_name):
    with open(file_name) as image:
        for line in image:
            line = line.strip('\n')
            print(chalk.magenta(line))
    input(chalk.blue('Press any key to continue...'))
    return


def answer_question(question, valid):
    choice = input(chalk.blue(question)).lower()
    while choice not in valid:
        choice = input(chalk.blue('Please enter a valid choice: '))
    return choice


def get_random_location():
    while True:
        r = random.randint(1, rows)
        c = random.randint(1, columns)
        if board[(r, c)] == None:
            return (r, c)


def get_valid_location(current_location):
    move_tuples = {'u':(-1,0), 'd':(1,0), 'l':(0,-1), 'r':(0,1)}
    while True:
        if hero:
            direction = answer_question("Which way do you want to go, 'u/d/l/r'?", ['u', 'd', 'l', 'r'])
            move_tuple = move_tuples[direction]
        else:
            move_tuple = random.choice([(-1,0), (1,0), (0,-1), (0,1)])

        next_location = (current_location[0] + move_tuple[0], current_location[1] + move_tuple[1])

        if 0 < next_location[0] <= rows and 0 < next_location[1] <= columns:
            return (next_location)
        print("You can't go that way.")




# Start Game

hero_name = input(chalk.blue('Hi, what is your name? '))
alive = True


# Initialize game
if answer_question(f'Do you want go on an adventure, {hero_name}?', ['y', 'n']) == 'y':

    fact_choices = ['fact1', 'fact2', 'fact3']
    friend_choices = ['troll']
    enemy_choices = ['ogre']
    booster_choices = ['nap', 'ham', 'energy', 'trap']
    weapon_choices = ['dagger', 'mace', 'sword', 'axe', 'lightning']

    strength_dictionary = {'dagger': 1, 'mace': 2, 'sword': 3, 'axe': 4, 'lightning': 5,
                           'nap': 2, 'ham': 5, 'energy': 3, 'trap': -5}

    icon_dictionary = {'treasure': 'T', 'map': 'M',
                       'dagger': 'W', 'mace': 'W', 'sword': 'W', 'axe': 'W', 'lightning': 'W',
                       'nap': 'B', 'ham': 'B', 'energy': 'B', 'trap': 'B',
                       'hero': '*', 'troll': 'F', 'unicorn': 'F',
                       'ogre': 'E', 'dragon': 'E'}
    rows = 15
    columns = 15

    found_map = False

    # Create an empty board
    board = dict((location, None) for location in
                        sorted(itertools.product([r for r in range(1, rows + 1)], [c for c in range(1, columns + 1)])))

    # Place the treasure
    location = get_random_location()
    treasure = Thing('treasure', False, location)
    board[location] = treasure

    # Place the treasure map
    location = get_random_location()
    map = Thing('map', False, location)
    board[location] = map

    # Place boosters and weapons
    boosters = list()
    weapons = list()
    for i in range(5):
        location = get_random_location()
        choice = random.choice(booster_choices)
        boosters.append(Thing(choice, False, location))
        board[location] = boosters[i]


    for i in range(2):
        location = get_random_location()
        choice = random.choice(weapon_choices)
        weapons.append(Thing(choice, False, location))
        board[location] = weapons[i]



    # Place characters
    location = get_random_location()
    hero = Character('hero', True, 50, 'dagger', location)
    board[location] = hero


    # Place friends
    friends = list()
    for i in range(3):
        location = get_random_location()
        friends.append(Character(random.choice(friend_choices), False, random.randint(10, 15), None, location))
        board[location] = friends[i]

    # Place enemies
    enemies = list()
    for i in range(3):
        location = get_random_location()
        enemies.append(Character(random.choice(enemy_choices), False,
                                  random.randint(10, 15), random.choice(weapon_choices), location))
        board[location] = enemies[i]


    print_image('hero.txt')

while alive:

    print(make_board_string(board))
    hero_status = 'Hero: ' + str(hero.get_location()) + ', Health: ' + str(hero.get_health()) + ', Weapon: ' + str(hero.get_weapon())
    if hero.get_health() > 35:
        print(chalk.green(hero_status))
    elif hero.get_health() > 10:
        print(chalk.yellow(hero_status))
    else:
        print(chalk.red(hero_status))


    # Move the hero


    old_location = hero.get_location()
    next_location = get_valid_location(old_location)

    # Moving to an empty location
    if board[next_location] == None:
        board[next_location] = hero
        hero.update_location(next_location)
        board[old_location] = None
        hero.update_health(-1)
        if hero.get_health() <= 0:
            print_image('death_by_exhaustion.txt')
            alive = False

    # Moving to an occupied location
    else:
        kind = board[next_location].get_kind()
        print_image(generate_filename(kind))
        if kind == 'treasure':
            break
        elif kind == 'map':
            found_map = True
            board[next_location] = hero
            hero.update_location(next_location)
            board[old_location] = None
            treasure.update_visible(True)
        elif kind in booster_choices:
            strength = strength_dictionary[kind]
            hero.update_health(strength)
            board[next_location] = hero
            hero.update_location(next_location)
            board[old_location] = None

        # Find a weapon
        elif kind in weapon_choices:
            found_weapon = kind
            current_weapon = hero.get_weapon()
            answer = answer_question('Do you want to trade take this weapon and leave your current one?', ['y', 'n'])
            if answer == 'y':
                print(chalk.blue('Great! Now you will really do some damage!'))
                board[next_location] = Thing(current_weapon, False, next_location)
                hero.update_weapon(found_weapon)
            else:
                print(chalk.blue('OK'))

        # Find a friendly troll
        elif kind == 'troll':
            print(chalk.blue('Trolls have the gift of knowledge...'))
            if found_map:
                print(chalk.blue('But I see you already have a map to the treasure'))
                answer = answer_question('Would you like to know an interesting fact? ',['y', 'n'])
                if answer == 'y':
                    print(chalk.blue(random.choice(fact_choices)))
                else:
                    print(chalk.blue('Okay. Have a nice day'))

            else:
                answer = answer_question('Would you like to know where you can find a map to the treasure? ', ['y', 'n'])
                if answer == 'y':
                    print(chalk.blue('You are a very smart hero indeed...'))
                    print(chalk.blue(f'You can find a map to the treasure in {map.get_location()}'))
                else:
                    print(chalk.blue('Suit yourself.'))

        elif kind == 'ogre':
            win = True
            enemy_name = board[next_location].get_kind().title()
            enemy_weapon = board[next_location].get_weapon()
            enemy_strength = strength_dictionary[enemy_weapon]
            hero_weapon = hero.get_weapon()
            hero_strength = strength_dictionary[hero_weapon]
            print(chalk.green(f"You are attacking a {kind} armed with a {enemy_weapon}"))
            answer = answer_question('Would you like to attack or run away (a/r)?', ['a', 'r'])
            while answer == 'a':
                battle_status = hero_name + ': ' + str(hero.get_health()) + '  vs.  ' + enemy_name + ': ' \
                                + str(board[next_location].get_health())
                if hero.get_health() > 35:
                    print(chalk.green(battle_status))
                elif hero.get_health() > 10:
                    print(chalk.yellow(battle_status))
                else:
                    print(chalk.red(battle_status))

                rps_dictionary = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
                answer = answer_question('Choose rock, paper, or scissors (r/p/s)', ['r', 'p', 's'])
                hero_choice = rps_dictionary[answer]
                enemy_choice = random.choice(['rock', 'paper', 'scissors'])

                print(chalk.green(f'You chose {good_guy_choice} and the enemy chose {bad_guy_choice}'))
                if enemy_choice == hero_choice:
                    print(chalk.green("It's a tie! Do over!"))
                elif enemy_choice == 'rock' and hero_choice == 'paper':
                    print(chalk.green("You've struck a blow! Good job!"))
                    board[next_location].update_health(-1 * hero_strength)
                elif enemy_choice == 'paper' and hero_choice == 'scissors':
                    print(chalk.green("You've struck a blow! Good job!"))
                    board[next_location].update_health(-1 * hero_strength)
                elif enemy_choice == 'scissors' and hero_choice == 'rock':
                    print(chalk.green("You've struck a blow! Good job!"))
                    board[next_location].update_health(-1 * hero_strength)
                elif enemy_choice == 'scissors' and hero_choice == 'paper':
                    print(chalk.red("You've taken a hit. Ouch!"))
                    hero.update_health(-1 * enemy_strength)
                elif enemy_choice == 'paper' and hero_choice == 'rock':
                    print(chalk.red("You've taken a hit. Ouch!"))
                    hero.update_health(-1 * enemy_strength)
                elif enemy_choice == 'rock' and hero_choice == 'scissors':
                    print(chalk.red("You've taken a hit. Ouch!"))
                    hero.update_health(-1 * enemy_strength)


                if board[next_location].get_health() <= 0:
                    print_image('won_the_battle.txt')
                    board[next_location] = Thing(enemy_weapon, False, next_location)
                    break
                if hero.get_health() <= 0:
                    print_image('died_in_battle.txt')
                    alive = False
                    break
                answer = answer_question('Would you like to attack or run away (a/r)?', ['a', 'r'])
