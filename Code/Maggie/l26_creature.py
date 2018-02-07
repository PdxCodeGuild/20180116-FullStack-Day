from l26_settings import *
from l26_graphics import *
from l26_gameboard import *
class Creature:  # all of the game objects are considered to be creatures
    def __init__(self, y_location, x_location, character, blocks_path, blocks_view=True):
        self.y_location = y_location
        self.x_location = x_location
        self.character = character
        self.color = WHITE
        self.blocks_path = blocks_path  # blocks movement
        self.seen = False  # is this currently visible to player?
        self.explored = False  # all spots start unexplored
        if self.seen:
            self.explored = True  # if the player is seeing it, then it's explored
        self.blocks_view = blocks_view  # does the occupant block view

    def move(self, dx, dy):
        from l26_main import board, creatures
        y_move = self.y_location + dy
        x_move = self.x_location + dx
        if y_move in range(board.height()) and x_move in range(board.width()):
            # if y_move not in creatures
            self.x_location += dx
            self.y_location += dy

    def put_on_board(self):
        render_and_blit_char(self.x_location, self.y_location, self.character, self.color)

class NPC(Creature):
    def __init__(self, y_location, x_location):
        super().__init__(y_location, x_location, 'ö',  blocks_path=True, blocks_view=False)

    def move(self, dx, dy):
        super().move(dx, dy)

class Player(Creature):
    def __init__(self, y_location, x_location):
        super().__init__(y_location, x_location, '@', blocks_path=False, blocks_view=False)

    def move(self, dx, dy):
            super().move(dx, dy)


# if __name__ == '__main__':
