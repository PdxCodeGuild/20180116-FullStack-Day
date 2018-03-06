"""Adventure Game!!! version 5

Introducing a board class
moving non-hero characters
"""

import random
import itertools
import chalk
import time

thing_dictionary = {'friends': ['troll', 'unicorn'],
                    'enemies': ['ogre', 'goblin'],
                    'boosters': ['nap', 'ham', 'energy', 'trap'],
                    'weapons': ['dagger', 'mace', 'sword', 'axe', 'lightning']
                    }

strength_dictionary = {'dagger': 1, 'mace': 2, 'sword': 3, 'axe': 4, 'lightning': 5, 'fire': 6,
                       'nap': 2, 'ham': 5, 'energy': 3, 'trap': -5}

icon_dictionary = {'treasure': '| 👑 ', 'map': '| 🗺️ ', 'castle': '| 🏰 ',
                   'dagger': '| 🗡️ ', 'mace': '| 🗡️ ', 'sword': '| 🗡️ ', 'axe': '| 🗡️ ', 'lightning': '| 🗡️ ',
                   'nap': '| 🌮 ', 'ham': '| 🌮 ', 'energy': '| 🌮 ', 'trap': '| 🌮 ',
                   'hero': '| 🌟 ', 'troll': '| 🧙️ ', 'unicorn': '| 🦄 ',
                   'ogre': '| 👹 ', 'goblin': '| 👿 ', 'dragon': '| 🐲 ', 'filler': '|    '}


class GameSpace():

    def __init__(self, name, rows, columns):
        self.name = name
        self.rows = rows
        self.columns = columns
        self.board = {location: Filler('filler', location, True) for location in
                         sorted(itertools.product([r for r in range(1, self.rows + 1)],
                                                  [c for c in range(1, self.columns + 1)]))}


    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def __str__(self):
        board_string = '-' + ('-----' * self.columns) + '\n'
        for row in range(1, self.rows + 1):
            for column in range(1, self.columns + 1):
                if self.board[row, column].is_visible():
                    board_string += self.board[row, column].get_icon()
                else:
                    board_string += '|    '

            board_string += '|\n'
            board_string += ('-' + ('-----' * self.columns) + '\n')
        return board_string

    def __getitem__(self, location):
        return self.board[location]

    def __setitem__(self, location, entity):
        self.board[location] = entity



class Thing:

    def __init__(self, kind, location, visible):
        self.kind = kind
        self.visible = visible
        self.location = location
        self.icon = icon_dictionary[self.kind]

    def get_icon(self):
        return self.icon

    def get_kind(self):
        return self.kind

    def get_location(self):
        return self.location

    def is_visible(self):
        return self.visible

    def update_location(self, location):
        self.location = location

    def update_visible(self, visible):
        self.visible = visible

class Filler(Thing):

    def __init__(self, kind, location, visible):
        Thing.__init__(self, kind, location, visible)


class Weapon(Thing):

    def __init__(self, kind, location, visible):
        Thing.__init__(self, kind, location, visible)


class Booster(Thing):

    def __init__(self, kind, location, visible):
        Thing.__init__(self, kind, location, visible)


class Friend(Thing):

    def __init__(self, kind, location, visible, level):
        Thing.__init__(self, kind, location, visible)
        self.level = round(float(level), 1)

    def get_level(self):
        return self.level


class Hero(Friend):

    def __init__(self, kind, location, visible, level, health, weapon):
        Friend.__init__(self, kind, location, visible, level)
        self.health = round(float(health), 1)
        self.weapon = weapon
        self.weapon_strength = strength_dictionary[self.weapon]
        self.attack_power = round(float(self.weapon_strength * (1 + (self.level - 1) / 10)), 1)

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
        self.attack_power = round(float(self.weapon_strength * (1 + (self.level - 1) / 10)), 1)

    def update_health(self, value):
        self.health = round(float(self.health + value), 1)

    def update_weapon(self, weapon):
        self.weapon = weapon
        self.weapon_strength = strength_dictionary[self.weapon]
        self.attack_power = round(float(self.weapon_strength * (1 + (self.level - 1) / 10)), 1)


    def __str__(self):
        fighter_stats = self.kind.title() + ':' + str(self.get_location()) + \
                        ', Health: ' + str(self.get_health()) + \
                        ', Level: ' + str(self.get_level()) + \
                        ', Weapon: ' + str(self.get_weapon()) + \
                        ', Weapon Strength: ' + str(self.get_weapon_strength()) + \
                        ', Attack Power: ' + str(self.get_attack_power())
        return fighter_stats


class Enemy(Hero):

    def __init__(self, kind, location, visible, level, health, weapon):
        Hero.__init__(self, kind, location, visible, level, health, weapon)


def update_board_visibility(world):
    hero_location = hero.get_location()
    for row in range(1, world.get_rows() + 1):
        for column in range(1, world.get_columns() + 1):
            if abs(hero_location[0] - row) + abs(hero_location[1] - column) <= 3:
                world[row, column].update_visible(True)
            else:
                world[row, column].update_visible(False)
    if found_map:
        castle.update_visible(True)
    hero.update_visible(True)

    return world


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


def get_random_location(world):
    rows = world.get_rows()
    columns = world.get_columns()
    while True:
        row = random.randint(1, rows)
        column = random.randint(1, columns)
        if isinstance(world[(row, column)], Filler):
            return row, column


def move_hero(location, world):
    move_tuples = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}
    while True:
        direction = answer_question("Which way do you want to go, 'u/d/l/r'?", ['u', 'd', 'l', 'r'])
        move_tuple = move_tuples[direction]
        choice = (location[0] + move_tuple[0], location[1] + move_tuple[1])
        if 0 < choice[0] <= world.get_rows() and 0 < choice[1] <= world.get_columns():
            return choice
        print("You can't go that way.")


def move_non_hero(location, world):
    move_tuples = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while True:
        move_tuple = random.choice(list(move_tuples.values()))
        choice = (location[0] + move_tuple[0], location[1] + move_tuple[1])
        if 0 < choice[0] <= world.get_rows() and 0 < choice[1] <= world.get_columns():
            return choice


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

    return good_guy, Filler('filler', location, True)


def battle(good_guy, bad_guy):
    good_strings = ["You've struck a blow! Good job!",
                   "You're doing great, keep it up!",
                   "That was an excellent hit!"]

    bad_strings = ["You've taken a hit. Ouch!",
                   "That's gonna leave a mark.",
                   "This is powerful enemy indeed!"]

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
        else:
            if bad_guy_choice == 'rock' and good_guy_choice == 'paper':
                hit = True
            elif bad_guy_choice == 'paper' and good_guy_choice == 'scissors':
                hit = True
            elif bad_guy_choice == 'scissors' and good_guy_choice == 'rock':
                hit = True
            elif bad_guy_choice == 'scissors' and good_guy_choice == 'paper':
                hit = False
            elif bad_guy_choice == 'paper' and good_guy_choice == 'rock':
                hit = False
            elif bad_guy_choice == 'rock' and good_guy_choice == 'scissors':
                hit = False

            if hit:
                print(chalk.green(random.choice(good_strings)))
                bad_guy.update_health(-1 * good_guy.get_attack_power())
            else:
                print(chalk.red(random.choice(bad_strings)))
                good_guy.update_health(-1 * bad_guy.get_attack_power())

        if good_guy.get_health() <= 0:
            print_image('died_in_battle.txt')
            return good_guy, bad_guy
        elif bad_guy.get_health() <= 0:
            print_image('won_the_battle.txt')
            if bad_guy.get_kind() == 'dragon':
                return good_guy, Filler('filler', bad_guy.get_location(), True)
            else:
                return good_guy, Weapon(bad_guy.get_weapon(), bad_guy.get_location(), False)

        battle_status = good_guy_name + ': ' + str(good_guy.get_health()) + '  vs.  ' + bad_guy_name + ': ' \
                        + str(bad_guy.get_health())

        if good_guy.get_health() > 35:
            print(chalk.green(battle_status))
        elif good_guy.get_health() > 10:
            print(chalk.yellow(battle_status))
        else:
            print(chalk.red(battle_status))

        ans = answer_question('Would you like to attack or run away (a/r)?', ['a', 'r'])
        if ans == 'r':
            print('Live to fight another day, brave hero.')

    return hero, bad_guy



alive = True

# Start Game

hero_name = input(chalk.blue('Hi, what is your name? ')).lower()
icon_dictionary[hero_name] = '| 🌟 '

answer = answer_question('Is this practice mode or normal mode? ' + hero_name.title(), ['p', 'n'])
if answer == 'p':
    practice = True
else:
    practice = False

answer = answer_question('Would you like to go on an adventure, ' + hero_name.title(), ['y', 'n'])
if answer == 'y':

    found_map = False

    # Create an empty board
    adventure_world = GameSpace('adventure world', 15, 15)

    # Place the castle
    location = get_random_location(adventure_world)
    castle = Thing('castle', location, True)
    adventure_world[location] = castle

    # Place the treasure map
    location = get_random_location(adventure_world)
    t_map = Thing('map', location, False)
    adventure_world[location] = t_map

    # Place boosters
    for i in range(5):
        location = get_random_location(adventure_world)
        adventure_world[location] = Booster(random.choice(thing_dictionary['boosters']), location, False)

    # Place weapon caches
    for i in range(3):
        location = get_random_location(adventure_world)
        adventure_world[location] = Weapon(random.choice(thing_dictionary['weapons']), location, False)


    # Place friends
    for i in range(5):
        location = get_random_location(adventure_world)
        adventure_world[location] = \
                    Friend(random.choice(thing_dictionary['friends']),
                    location, False, random.randint(1, 3))

    # Place the hero
    location = get_random_location(adventure_world)
    hero = Hero(hero_name, location, True, 1, 50, 'dagger')
    adventure_world[location] = hero
    found_map = False

    # Place enemies
    for i in range(5):
        location = get_random_location(adventure_world)
        if practice:
            adventure_world[location] = Enemy('ogre', location, False, 1, 5, 'dagger') # Weak practice enemies
        else:
            adventure_world[location] = \
                    Enemy(random.choice(thing_dictionary['enemies'][0:2]), location, False,
                    random.randint(1, 3), random.randint(10, 15), random.choice(thing_dictionary['weapons']))



    print_image('hero.txt')


else:
    alive = False

while alive:
    update_board_visibility(adventure_world)
    print(adventure_world)
    if hero.get_health() > 35:
        print(chalk.green(hero))
    elif hero.get_health() > 10:
        print(chalk.yellow(hero))
    else:
        print(chalk.red(hero))

    # Move the hero
    current_location = hero.get_location()
    next_location = move_hero(current_location, adventure_world)

    # Moving to an empty location
    if isinstance(adventure_world[next_location], Filler):
        hero.update_location(next_location)
        adventure_world[next_location] = hero
        adventure_world[current_location] = Filler('filler', location, True)
        hero.update_health(-1)
        if hero.get_health() <= 0:
            print_image('death_by_exhaustion.txt')
            alive = False

    # Moving to an occupied location
    else:
        print_image(adventure_world[next_location].get_kind() + '.txt')
        if isinstance(adventure_world[next_location], Enemy):
            hero, adventure_world[next_location] = battle(hero, adventure_world[next_location])

        elif isinstance(adventure_world[next_location], Friend):
            hero, adventure_world[next_location] = friendly_interaction(hero, adventure_world[next_location])

        elif adventure_world[next_location] == castle:
                answer = answer_question('You are about to enter the castle, are you sure you want to do this? ',
                                         ['y', 'n'])
                if answer == 'y':
                    break

        elif adventure_world[next_location] == t_map:
            found_map = True
            hero.update_location(next_location)
            adventure_world[next_location] = hero
            adventure_world[next_location] = Filler('filler', location, True)
            castle.update_visible(True)
        elif isinstance(adventure_world[next_location], Booster):
            strength_dictionary[adventure_world[next_location].get_kind()]
            hero.update_health(strength_dictionary[adventure_world[next_location].get_kind()])
            adventure_world[next_location] = hero
            hero.update_location(next_location)
            adventure_world[next_location] = Filler('filler', location, True)
        elif isinstance(adventure_world[next_location], Weapon):
            found_weapon = adventure_world[next_location].get_kind()
            current_weapon = hero.get_weapon()
            answer = answer_question('Do you want to trade take this weapon and leave your current one?', ['y', 'n'])
            if answer == 'y':
                print(chalk.blue('Great! Now you will really do some damage!'))
                adventure_world[next_location] = Weapon(current_weapon, next_location, False)
                hero.update_weapon(found_weapon)
            else:
                print(chalk.blue('OK'))

    # Moving movable characters, besure to check here for occupied space

if alive:

    castle_world = GameSpace('castle', 8, 8)

    # Place the hero
    hero.update_location((1, 1))
    castle_world[(1, 1)] = hero

    # Place the treasure
    location = get_random_location(castle_world)
    treasure = Thing('treasure', location, True)
    castle_world[location] = treasure

    # Place the dragon
    location = get_random_location(castle_world)
    if practice:
        dragon = Enemy('dragon', location, True, 1, 5, 'dagger')  # Weak practice dragon
    else:
        dragon = Enemy('dragon', location, True, random.randint(3, 5), random.randint(20, 25), 'fire') # Regular dragon
    castle_world[location] = dragon

    dragon_dead = False

while alive:
    print(castle_world)

    if hero.get_health() > 35:
        print(chalk.green(hero))
    elif hero.get_health() > 10:
        print(chalk.yellow(hero))
    else:
        print(chalk.red(hero))

    current_location = hero.get_location()
    next_location = move_hero(current_location, castle_world)

    # Moving to an empty location
    if isinstance(castle_world[next_location], Filler):
        hero.update_location(next_location)
        castle_world[next_location] = hero
        castle_world[current_location] = Filler('filler', location, True)
        hero.update_health(-1)
        if hero.get_health() <= 0:
            print_image('death_by_exhaustion.txt')
            alive = False
    else:
        if castle_world[next_location] == treasure and dragon_dead:
            print_image('treasure.txt')
            break
        if castle_world[next_location] == treasure and not dragon_dead:
            print("You have to slay the dragon before you can take the treasure")
        if castle_world[next_location] == dragon:
            print_image('dragon.txt')
            hero, castle_world[next_location] = battle(hero, castle_world[next_location])
            if isinstance(castle_world[next_location], Filler):
                dragon_dead = True





