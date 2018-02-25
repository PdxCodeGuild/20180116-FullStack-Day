"""Lab 26"""
import random


# make enemy loop through rows

class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Tree(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, 'Ѧ')


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, 'ּϠ')


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, 'Ϣ')


class Board:
    def __init__(self, width, height):
        self.board = []
        for i in range(height):  # loop over the rows
            self.board.append([])  # append an empty row
            for j in range(width):  # loop over the columns
                self.board[i].append('x')  # append an empty space to the board

    def random_location(self):
        return random.randint(0, self.width() - 1), random.randint(0, self.height() - 1)

    def __getitem__(self, j):
        return self.board[j]

    def width(self):
        return len(self.board[0])

    def height(self):
        return len(self.board[0])

    def print(self, entities):
        for i in range(self.height()):
            for j in range(self.width()):
                for k in range(len(entities)):
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else:
                    print(' ', end='')
            print()


b = Board(50, 25)

pi, pj = b.random_location()
player = Player(pi, pj)

entities = [player]
enemies = []

for i in range(100):
    ei, ej = b.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)
print('You are a speck of consciousness observing the solar system. Find a wormhole to enter an alternate reality')
while True:

    b.print(entities)

    command = input('Go somewhere: ')  # get the command from the user
    if player.location_j >= 50:
        print('You have gone through a wormhole to escape the solar system, hyperspace, and entered an alternate reality.')
        print('You are now a person again and don\'t remember your interdimensional travels')
        break
    elif command == 'one':
        print('You have entered the void. You no longer exist')
        break  # exit the game and win

    elif command == 'teleport':
        player.location_j -= 5  # move left 5 spaces
        print('You have teleported out of the solar system but now you are stuck in hyperspace. Find a wormhole to go back into the solar system, then find another another wormhole to enter an alternate reality that you have created.')
    elif command == 'wormhole':
        player.location_j += 10  # move right 10 spaces
    elif command == 'up':
        player.location_i -= 1  # move up
    elif command == 'down':
        player.location_i += 1  # move down

    for enemy in enemies:
        if random.randint(0, 1) == 0:
            enemy.location_i += random.randint(-1, 1)
