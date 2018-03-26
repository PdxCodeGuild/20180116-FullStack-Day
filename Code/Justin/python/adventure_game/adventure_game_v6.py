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
                   'ogre': '| 👹 ', 'goblin': '| 👿 ', 'dragon': '| 🐲 ', 'empty': '|    '}


class GameSpace():

    def __init__(self, type, rows, columns):
        self.type = type
        self.rows = rows
        self.columns = columns
        self.board = {location: Empty('empty', location, True) for location in
                         sorted(itertools.product([r for r in range(1, self.rows + 1)],
                                                  [c for c in range(1, self.columns + 1)]))}

    def get_type(self):
        return self.type

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_enemies(self):
        return [entity for entity in list(self.board.values()) if isinstance(entity, Enemy)]

    def get_entities(self):
        return [entity for entity in list(self.board.values())]

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


class Empty(Thing):

    def __init__(self, kind, location, visible):
        Thing.__init__(self, kind, location, visible)


class Weapon(Thing):

    def __init__(self, kind, location, visible):
        Thing.__init__(self, kind, location, visible)


class Map(Thing):

    def __init__(self, kind, location, visible):
        Thing.__init__(self, kind, location, visible)


class Castle(Thing):

    def __init__(self, kind, location, visible):
        Thing.__init__(self, kind, location, visible)

class Treasure(Thing):

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


def build_gamespace(name, rows, columns, num_boosters, num_weapons, num_friends, num_enemies):
    # Create an empty board
    world = GameSpace(name, rows, columns)

    # Place boosters
    for i in range(num_boosters):
        location = get_random_location(world)
        world[location] = Booster(random.choice(thing_dictionary['boosters']), location, True)

    # Place weapon caches
    for i in range(num_weapons):
        location = get_random_location(world)
        world[location] = Weapon(random.choice(thing_dictionary['weapons']), location, True)

    # Place friends
    for i in range(num_friends):
        location = get_random_location(world)
        world[location] = \
                    Friend(random.choice(thing_dictionary['friends']),
                    location, True, random.randint(1, 3))

    # Place enemies
    for i in range(num_enemies):
        location = get_random_location(world)
        if practice:
            world[location] = Enemy('ogre', location, True, 1, 5, 'dagger') # Weak practice enemies
        else:
            world[location] = \
                    Enemy(random.choice(thing_dictionary['enemies'][0:2]), location, True,
                    random.randint(1, 3), random.randint(10, 15), random.choice(thing_dictionary['weapons']))

    return world


def update_board_visibility(world):
    hero_location = hero.get_location()
    for row in range(1, world.get_rows() + 1):
        for column in range(1, world.get_columns() + 1):
            world[row, column].update_visible(True)
            if not practice:
                if abs(hero_location[0] - row) + abs(hero_location[1] - column) > 3:
                    world[row, column].update_visible(False)
    if found_map:
        for entity in world.get_entities():
            if isinstance(entity, Castle):
                entity.update_visible(True)
    return world


def print_board(world):
    update_board_visibility(world)
    print(world)
    if hero.get_health() > 35:
        print(chalk.green(hero))
    elif hero.get_health() > 10:
        print(chalk.yellow(hero))
    else:
        print(chalk.red(hero))
    time.sleep(2)
    return


def print_image(file_name):
    file_name = 'adventure_game/' + file_name
    with open(file_name, 'r') as image:
        lines = [line.rstrip() for line in image]
        audio = lines.pop(0)
        for line in lines:
            print(chalk.magenta(line))
    time.sleep(2)
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
        if isinstance(world[(row, column)], Empty):
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


def move_enemies(world, hero):
    # Moving enemies around the board, if chosen direction is empty or hero, action is taken, otherwise they don't mainLoop.
    # Build list of enemies first then mainLoop them one at a time
    move_tuples = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    enemies = world.get_enemies()
    for enemy in enemies:
        print(enemy.get_kind())
        current_location = enemy.get_location()
        while True:
            choice = random.choice(move_tuples)
            next_location = (current_location[0] + choice[0], current_location[1] + choice[1])
            if 0 < next_location[0] <= world.get_rows() and 0 < next_location[1] <= world.get_columns():
                break
        if isinstance(world[next_location], Empty):
            world[next_location] = enemy
            enemy.update_location(next_location)
            world[current_location] = Empty('empty', current_location, True)
        elif world[next_location] == hero:
            print_image(enemy.get_kind() + '.txt')
            print(chalk.red(f"Look out! You are being attacked by a {enemy.get_kind()}"))
            world[current_location] = battle(enemy)
    return


def friendly_interaction(good_guy, friend):
    file_name = 'adventure_game/' + friend.get_kind() + '_dialog.txt'
    with open(file_name, 'r') as dialog:
        lines = [line.strip() for line in dialog]

    print(chalk.blue(lines[0]))
    time.sleep(2)
    if (hero.get_health() >= 60 and friend.get_kind() == 'unicorn') or (found_map and friend.get_kind() == 'troll'):
        print(chalk.blue(lines[1]))
        ans = answer_question(lines[2], ['y', 'n'])
        time.sleep(2)
        if ans == 'y':
            print(chalk.blue(random.choice(lines[3:6])))
        else:
            print(chalk.blue(lines[6]))

    else:
        ans = answer_question(lines[7], ['y', 'n'])
        time.sleep(2)
        if ans == 'n':
            print(chalk.blue(lines[10]))
        else:
            print(chalk.blue(lines[8]))
            if friend.get_kind() == 'troll':
                print(chalk.blue(lines[9] + ' ' + str(t_map.get_location())))
            elif friend.get_kind() == 'unicorn':
                good_guy.update_health(60 - good_guy.get_health())
    time.sleep(3)
    print(chalk.blue('You have also earned some experience points'))
    time.sleep(2)
    hero.update_level(friend.get_level())

    return good_guy, Empty('empty', location, True)


def battle(enemy):
    good_strings = ["You've struck a blow! Good job!",
                    "You're doing great, keep it up!",
                    "That was an excellent hit!"]

    bad_strings = ["You've taken a hit. Ouch!",
                   "That's gonna leave a mark.",
                   "This is a powerful enemy indeed!"]

    print(chalk.yellow(f"You are attacking a {enemy.get_kind()}, armed with a {enemy.get_weapon()}."))
    print(chalk.yellow("Here are it's stats..."))
    time.sleep(2)
    print(chalk.green(enemy))
    time.sleep(2)
    ans = answer_question('Would you like to attack or run away (a/r)?', ['a', 'r'])
    while ans == 'a':
        rps_dictionary = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        ans = answer_question('Choose rock, paper, or scissors (r/p/s)', ['r', 'p', 's'])
        hero_choice = rps_dictionary[ans]
        enemy_choice = random.choice(['rock', 'paper', 'scissors'])

        print(chalk.yellow(f'You chose {hero_choice} and the enemy chose {enemy_choice}'))
        if enemy_choice == hero_choice:
            print(chalk.yellow("It's a tie! Do over!"))
        else:
            if enemy_choice == 'rock' and hero_choice == 'paper':
                hit = True
            elif enemy_choice == 'paper' and hero_choice == 'scissors':
                hit = True
            elif enemy_choice == 'scissors' and hero_choice == 'rock':
                hit = True
            elif enemy_choice == 'scissors' and hero_choice == 'paper':
                hit = False
            elif enemy_choice == 'paper' and hero_choice == 'rock':
                hit = False
            elif enemy_choice == 'rock' and hero_choice == 'scissors':
                hit = False

            if hit:
                print(chalk.green(random.choice(good_strings)))
                enemy.update_health(-1 * hero.get_attack_power())
            else:
                print(chalk.red(random.choice(bad_strings)))
                hero.update_health(-1 * enemy.get_attack_power())

        if hero.get_health() <= 0:
            print_image('died_in_battle.txt')
            return enemy
        elif enemy.get_health() <= 0:
            print_image('won_the_battle.txt')
            if enemy.get_kind() == 'dragon':
                return Empty('empty', enemy.get_location(), True)
            else:
                return Weapon(enemy.get_weapon(), enemy.get_location(), True)

        battle_status = hero.get_kind().title() + ': ' + str(hero.get_health()) + '  vs.  ' + \
                        enemy.get_kind().title() + ': ' + str(enemy.get_health())

        if hero.get_health() > 35:
            print(chalk.green(battle_status))
        elif hero.get_health() > 10:
            print(chalk.yellow(battle_status))
        else:
            print(chalk.red(battle_status))

        ans = answer_question('Would you like to attack or run away (a/r)?', ['a', 'r'])
        if ans == 'r':
            print('Live to fight another day, brave hero.')

    return enemy


# Start Game
hero_name = input(chalk.blue('Hi, what is your name? ')).lower()
icon_dictionary[hero_name] = '| 🌟 '

# Choose practice mode or normal mode
answer = answer_question('Is this practice mode or normal mode? (p/n) ', ['p', 'n'])
if answer == 'p':
    practice = True
else:
    practice = False


answer = answer_question(f'Would you like to go on an adventure, {hero_name.title()}? (y/n) ' +
                         hero_name.title(), ['y', 'n'])
if answer == 'y':

    adventure_world = build_gamespace('adventure world', 15, 15, 5, 3, 5, 5)

    # Place the castle
    location = get_random_location(adventure_world)
    adventure_world[location] = Castle('castle', location, True)

    # Place the treasure map
    location = get_random_location(adventure_world)
    t_map = Map('map', location, True)

    adventure_world[location] = t_map

    # Place the hero
    location = get_random_location(adventure_world)
    hero = Hero(hero_name, location, True, 1, 50, 'dagger')
    adventure_world[location] = hero
    found_map = False
    alive = True
    print_image('hero.txt')


else:
    alive = False

# Adventure World
print('\n\n\n')
print_image('adventure_world.txt')
print_board(adventure_world)


while alive:

    #Get location for the hero's next mainLoop
    current_location = hero.get_location()
    next_location = move_hero(current_location, adventure_world)

    #If next location is empty
    if isinstance(adventure_world[next_location], Empty):
        hero.update_location(next_location)
        adventure_world[next_location] = hero
        adventure_world[current_location] = Empty('empty', current_location, True)
        hero.update_health(-1)
        if hero.get_health() <= 0:
            print_image('death_by_exhaustion.txt')
            alive = False

    #If the next location is occupied
    else:
        print_image(adventure_world[next_location].get_kind() + '.txt')
        # If the next location is an enemy, go to battle function
        if isinstance(adventure_world[next_location], Enemy):
            adventure_world[next_location] = battle(adventure_world[next_location])
        # If the next location is a friend, go to friendly interaction function
        elif isinstance(adventure_world[next_location], Friend):
            adventure_world[next_location] = friendly_interaction(adventure_world[next_location])
        # If the next location is the castle...
        elif isinstance(adventure_world[next_location], Castle):
                answer = answer_question('You are about to enter the castle, are you sure you want to do this? ',
                                         ['y', 'n'])
                if answer == 'y':
                    break
        # If the next location is the map...
        elif isinstance(adventure_world[next_location], Map):
            found_map = True
            hero.update_location(next_location)
            adventure_world[next_location] = hero
            adventure_world[current_location] = Empty('empty', location, True)
            for entity in adventure_world.get_entities():
                if isinstance(entity, Castle):
                    entity.update_visible(True)

        # If the next location is a booster...
        elif isinstance(adventure_world[next_location], Booster):
            hero.update_health(strength_dictionary[adventure_world[next_location].get_kind()])
            adventure_world[next_location] = hero
            hero.update_location(next_location)
            adventure_world[current_location] = Empty('empty', location, True)
        # If the next location is a weapon...
        elif isinstance(adventure_world[next_location], Weapon):
            found_weapon = adventure_world[next_location].get_kind()
            current_weapon = hero.get_weapon()
            answer = answer_question('Do you want to trade take this weapon and leave your current one? (y/n)',
                                     ['y', 'n'])
            if answer == 'y':
                print(chalk.blue('Great! Now you will really do some damage!'))
                adventure_world[next_location] = Weapon(current_weapon, next_location, True)
                hero.update_weapon(found_weapon)
            else:
                print(chalk.blue('OK'))

    # Print Board after hero moves
    print_board(adventure_world)

    # Moving the enemies
    move_enemies(adventure_world, hero)

    # Print board after enemies mainLoop
    print_board(adventure_world)


# Moving into Castle World
if alive:

    # Create Castle World
    castle_world = build_gamespace('castle', 8, 8, 2, 1, 0, 2)

    # Add the dragon
    location = get_random_location(castle_world)
    if practice:
        dragon = Enemy('dragon', location, True, 1, 5, 'dagger')  # Weak practice dragon
    else:
        dragon = Enemy('dragon', location, True, random.randint(3, 5), random.randint(20, 25), 'fire')  # Regular dragon
    castle_world[location] = dragon
    dragon_dead = False  # Treasure can only be taken if the dragon is dead

    # Add the Treasure
    location = get_random_location(castle_world)
    treasure = Thing('treasure', location, True)
    castle_world[location] = treasure

    # Place the hero
    location = get_random_location(castle_world)
    hero.update_location(location)
    castle_world[location] = hero

    print_board(castle_world)


while alive:  # Currently in castle world

    # Get next location for the hero
    current_location = hero.get_location()
    next_location = move_hero(current_location, castle_world)

    # Moving to an empty location
    if isinstance(castle_world[next_location], Empty):
        hero.update_location(next_location)
        castle_world[next_location] = hero
        castle_world[current_location] = Empty('empty', location, True)
        hero.update_health(-1)
        if hero.get_health() <= 0:
            print_image('death_by_exhaustion.txt')
            alive = False

    else:
        if isinstance(castle_world[next_location], Booster):
            hero.update_health(strength_dictionary[adventure_world[next_location].get_kind()])
            castle_world[next_location] = hero
            hero.update_location(next_location)
            adventure_world[current_location] = Empty('empty', location, True)
        # If the next location is a weapon...
        elif isinstance(castle_world[next_location], Weapon):
            found_weapon = adventure_world[next_location].get_kind()
            current_weapon = hero.get_weapon()
            answer = answer_question('Do you want to trade take this weapon and leave your current one? (y/n)',
                                     ['y', 'n'])
            if answer == 'y':
                print(chalk.blue('Great! Now you will really do some damage!'))
                adventure_world[next_location] = Weapon(current_weapon, next_location, True)
                hero.update_weapon(found_weapon)
            else:
                print(chalk.blue('OK'))
        elif isinstance(castle_world[next_location], Treasure) and dragon_dead:
            print_image('treasure.txt')
            break
        elif isinstance(castle_world[next_location], Treasure) and not dragon_dead:
            print("You have to slay the dragon before you can take the treasure")
        elif isinstance(castle_world[next_location], Enemy):
            print_image(castle_world[next_location].get_kind() + 'txt')
            castle_world[next_location] = battle(castle_world[next_location])
            if isinstance(castle_world[next_location], Empty):
                dragon_dead = True


    # Print Board after hero moves
    print_board(castle_world)

    # Moving the dragon
    move_enemies(castle_world, hero)

    # Print Board after enemies mainLoop
    print_board(castle_world)




