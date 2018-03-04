"""Adventure Game!!! version 2"""

import random
import itertools
import chalk

thing_dictionary = {'friends': ['troll', 'unicorn'],
                    'enemies': ['ogre', 'dragon'],
                    'boosters': ['nap', 'ham', 'energy', 'trap'],
                    'weapons': ['dagger', 'mace', 'sword', 'axe', 'lightning']
                    }

strength_dictionary = {'dagger': 1, 'mace': 2, 'sword': 3, 'axe': 4, 'lightning': 5,
                       'nap': 2, 'ham': 5, 'energy': 3, 'trap': -5}

icon_dictionary = {'treasure': 'T', 'map': 'M',
                   'dagger': 'W', 'mace': 'W', 'sword': 'W', 'axe': 'W', 'lightning': 'W',
                   'nap': 'B', 'ham': 'B', 'energy': 'B', 'trap': 'B',
                   'hero': '*', 'troll': 'F', 'unicorn': 'U',
                   'ogre': 'O', 'dragon': 'D', 'castle': 'C'}


# class World():
#     def __init__(self, rows, columns):


class Thing:

    def __init__(self, kind, location, visible, mobile):
        self.kind = kind
        self.visible = visible
        self.mobile = mobile
        self.location = location

    def get_kind(self):
        return self.kind

    def get_location(self):
        return self.location

    def get_visible(self):
        return self.visible

    def get_mobile(self):
        return self.mobile

    def update_location(self, location):
        self.location = location

    def update_visible(self, visible):
        self.visible = visible

    def update_mobile(self, mobile):
        self.mobile = mobile


class Character(Thing):

    def __init__(self, kind, location, visible, mobile, level):
        Thing.__init__(self, kind, location, visible, mobile)
        self.level = round(float(level), 1)

    def get_level(self):
        return self.level


class Fighter(Character):

    def __init__(self, kind, location, visible, mobile, level, health, weapon):
        Character.__init__(self, kind, location, visible, mobile, level)
        self.health = round(float(health), 1)
        self.weapon = weapon
        self.weapon_strength = strength_dictionary[self.weapon]
        self.attack_power = round(float(self.weapon_strength * (1 + (self.level - 1) / 10), 1))

    def get_health(self):
        return self.health

    def get_weapon(self):
        return self.weapon

    def get_weapon_strength(self):
        return self.weapon_strength

    def get_attack_power(self):
        return self.attack_power

    def update_level(self, value):
        self.level += value
        self.attack_power = round(float(self.weapon_strength * (1 + (self.level - 1) / 10), 1))

    def update_health(self, value):
        self.health = round(float(self.health + value), 1)

    def update_weapon(self, weapon):
        self.weapon = weapon
        self.weapon_strength = strength_dictionary[self.weapon]
        self.attack_power = round(float(self.weapon_strength * (1 + (self.level - 1) / 10), 1))


    def __str__(self):
        fighter_stats = self.kind.title() + ':' + str(self.get_location()) + \
                        ', Health: ' + str(self.get_health()) + \
                        ', Level: ' + str(self.get_level()) + \
                        ', Weapon: ' + str(self.get_weapon()) + \
                        ', Weapon Strength: ' + str(self.get_weapon_strength()) + \
                        ', Attack Power: ' + str(self.get_attack_power())



        return fighter_stats

def make_board(rows, columns):
    return dict((location, None) for location in
         sorted(itertools.product([r for r in range(1, rows + 1)], [c for c in range(1, columns + 1)])))

def make_board_string(board):
    # Update visibility
    hero_r = hero.get_location()[0]
    hero_c = hero.get_location()[1]
    for r in range(1, rows + 1):
        for c in range(1, columns + 1):
            if board[(r, c)] in [None, hero]:
                continue
            if (abs(hero_r - r) + abs(hero_c - c)) <= 3:
                board[(r, c)].update_visible(True)
            else:
                board[(r, c)].update_visible(False)
    if found_map:
        castle.update_visible(True)

    # Construct string
    board_string = ''
    for r in range(1, rows + 1):
        board_string = board_string + '-' + ('----' * columns) + '\n'
        for c in range(1, columns + 1):
            if board[(r, c)] is None or not board[(r, c)].get_visible():
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
        choice = input('Please enter a valid choice: ')
    return choice


def get_random_location():
    while True:
        r = random.randint(1, rows)
        c = random.randint(1, columns)
        if board[(r, c)] is None:
            return r, c


def get_valid_location(current_location):
    move_tuples = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}
    while True:
        if hero:
            direction = answer_question("Which way do you want to go, 'u/d/l/r'?", ['u', 'd', 'l', 'r'])
            move_tuple = move_tuples[direction]
        else:
            move_tuple = random.choice([(-1,0), (1,0), (0,-1), (0,1)])

        next_location = (current_location[0] + move_tuple[0], current_location[1] + move_tuple[1])

        if 0 < next_location[0] <= rows and 0 < next_location[1] <= columns:
            return next_location
        print("You can't go that way.")

def friendly_interaction(good_guy, friend):
    file_name = friend.get_kind() + '_dialog.txt'
    with open(file_name) as dialog:
        lines = [line.strip() for line in dialog]
        print(chalk.blue(lines[0]))
        if (hero.get_health() >= 60 and friend.get_kind() == 'unicorn') or (found_map and friend.get_kind() == 'troll'):
            print(chalk.blue(lines[1]))
            ans = answer_question(lines[2], ['y', 'n'])
            if ans == 'y':
                print(chalk.blue(random.choice(lines[3:6])))
            else:
                print(chalk.blue(lines[6]))

        else:
            ans = answer_question(lines[7], ['y', 'n'])
            if ans == 'n':
                print(chalk.blue(lines[10]))
            else:
                print(chalk.blue(lines[8]))
                if friend.get_kind() == 'troll':
                    print(chalk.blue(lines[9] + ' ' + str(t_map.get_location())))
                elif friend.get_kind() == 'unicorn':
                    good_guy.update_health(60 - good_guy.get_health())

    print(chalk.blue('You have also earned some experience points'))
    hero.update_level(friend.get_level())

    return good_guy, None

def battle(good_guy, bad_guy):
    bad_guy_name = bad_guy.get_kind().title()
    good_guy_name = good_guy.get_kind().title()

    print(chalk.green(f"You are attacking a {bad_guy.get_kind()}, armed with a {bad_guy.get_weapon()}"))
    print(chalk.green("here are it's stats..."))
    print(chalk.green(bad_guy))
    ans = answer_question('Would you like to attack or run away (a/r)?', ['a', 'r'])
    while ans == 'a':
        rps_dictionary = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        ans = answer_question('Choose rock, paper, or scissors (r/p/s)', ['r', 'p', 's'])
        good_guy_choice = rps_dictionary[ans]
        bad_guy_choice = random.choice(['rock', 'paper', 'scissors'])

        print(chalk.green(f'You chose {good_guy_choice} and the enemy chose {bad_guy_choice}'))
        if bad_guy_choice == good_guy_choice:
            print(chalk.green("It's a tie! Do over!"))
        elif bad_guy_choice == 'rock' and good_guy_choice == 'paper':
            print(chalk.green("You've struck a blow! Good job!"))
            bad_guy.update_health(-1 * good_guy.get_attack_power())
        elif bad_guy_choice == 'paper' and good_guy_choice == 'scissors':
            print(chalk.green("You've struck a blow! Good job!"))
            bad_guy.update_health(-1 * good_guy.get_attack_power())
        elif bad_guy_choice == 'scissors' and good_guy_choice == 'rock':
            print(chalk.green("You've struck a blow! Good job!"))
            bad_guy.update_health(-1 * good_guy.get_attack_power())
        elif bad_guy_choice == 'scissors' and good_guy_choice == 'paper':
            print(chalk.red("You've taken a hit. Ouch!"))
            good_guy.update_health(-1 * bad_guy.get_attack_power())
        elif bad_guy_choice == 'paper' and good_guy_choice == 'rock':
            print(chalk.red("You've taken a hit. Ouch!"))
            good_guy.update_health(-1 * bad_guy.get_attack_power())
        elif bad_guy_choice == 'rock' and good_guy_choice == 'scissors':
            print(chalk.red("You've taken a hit. Ouch!"))
            good_guy.update_health(-1 * bad_guy.get_attack_power())

        if hero.get_health() <= 0:
            print_image('died_in_battle.txt')
            return good_guy, bad_guy
        elif bad_guy.get_health() <= 0:
            print_image('won_the_battle.txt')
            return good_guy, Thing(bad_guy.get_weapon(), bad_guy.get_location(), False, False)

        battle_status = good_guy_name + ': ' + str(good_guy.get_health()) + '  vs.  ' + bad_guy_name + ': ' \
                        + str(bad_guy.get_health())
        if good_guy.get_health() > 35:
            print(chalk.green(battle_status))
        elif good_guy.get_health() > 10:
            print(chalk.yellow(battle_status))
        else:
            print(chalk.red(battle_status))

        ans = answer_question('Would you like to attack or run away (a/r)?', ['a', 'r'])

    return hero, bad_guy





alive = True

# Start Game

hero_name = input(chalk.blue('Hi, what is your name? '))
answer = answer_question('Would you like to go on an adventure, ' + hero_name, ['y', 'n'])
if answer == 'y':

    found_map = False

    # Create an empty board
    rows = 15
    columns = 15
    board = make_board(rows, columns)

    # Place the castle
    location = get_random_location()
    castle = Thing('castle', location, False, False)
    board[location] = castle

    # Place the treasure map
    location = get_random_location()
    t_map = Thing('map', location, False, False)
    board[location] = t_map

    # Place boosters
    for i in range(5):
        location = get_random_location()
        board[location] = Thing(random.choice(thing_dictionary['boosters']), location, False, False)

    # Place weapon caches
    for i in range(3):
        location = get_random_location()
        board[location] = Thing(random.choice(thing_dictionary['weapons']), location, False, False)


    # Place friends
    for i in range(5):
        location = get_random_location()
        board[location] = Character(random.choice(thing_dictionary['friends']), location, False, True, random.randint(1, 3))

    # Place the hero
    location = get_random_location()
    icon_dictionary[hero_name] = '*'
    hero = Fighter(hero_name, location, True, True, 1, 50, 'dagger')
    board[location] = hero

    # Place enemies
    for i in range(5):
        location = get_random_location()
        board[location] = Fighter(random.choice(thing_dictionary['enemies'][0:1]),
                                  location, False, True,
                                  random.randint(1, 3), random.randint(10, 15),
                                  random.choice(thing_dictionary['weapons']))

    print_image('hero.txt')


else:
    alive = False

while alive:
    print(make_board_string(board))
    if hero.get_health() > 35:
        print(chalk.green(hero))
    elif hero.get_health() > 10:
        print(chalk.yellow(hero))
    else:
        print(chalk.red(hero))

    # Move the hero
    old_location = hero.get_location()
    next_location = get_valid_location(old_location)

    # Moving to an empty location
    if board[next_location] is None:
        board[next_location] = hero
        hero.update_location(next_location)
        board[old_location] = None
        hero.update_health(-1)
        if hero.get_health() <= 0:
            print_image('death_by_exhaustion.txt')
            alive = False

    # Moving to an occupied location
    else:
        print_image(board[next_location].get_kind() + '.txt')
        if isinstance(board[next_location], Fighter):
            hero, board[next_location] = battle(hero, board[next_location])

        elif isinstance(board[next_location], Character):
            hero, board[next_location] = friendly_interaction(hero, board[next_location])


        else:
            if board[next_location] == castle:
                answer = answer_question('You are about to enter the castle, are you sure you want to do this? ',
                                         ['y', 'n'])
                if answer == 'y':
                    break
            elif board[next_location] == t_map:
                found_map = True
                board[next_location] = hero
                hero.update_location(next_location)
                board[old_location] = None
                castle.update_visible(True)
            elif board[next_location].get_kind() in thing_dictionary['boosters']:
                strength = strength_dictionary[board[next_location].get_kind()]
                hero.update_health(strength)
                board[next_location] = hero
                hero.update_location(next_location)
                board[old_location] = None
            elif board[next_location].get_kind() in thing_dictionary['weapons']:
                found_weapon = board[next_location].get_kind()
                current_weapon = hero.get_weapon()
                answer = answer_question('Do you want to trade take this weapon and leave your current one?', ['y', 'n'])
                if answer == 'y':
                    print(chalk.blue('Great! Now you will really do some damage!'))
                    board[next_location] = Thing(current_weapon, next_location, False, False)
                    hero.update_weapon(found_weapon)
                else:
                    print(chalk.blue('OK'))

    # Moving movable characters
    for character in board.values():
        if character is not None:
            break

# Entering the castle
while alive:
    castle_board = make_board(8, 8)
    break



