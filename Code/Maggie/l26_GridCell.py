
class GridCell:  # properties of cells within the play area
    def __init__(self, character, color):
        self.character = character
        self.color = color
        self.blocks_path = False  # blocks movement
        self.seen = False  # is this currently visible to player?
        self.explored = False  # all spots start unexplored
        self.occupied = False
        self.contents = []
        if self.seen:
            self.explored = True  # if the player is seeing it, then it's explored

    def path_blocked(self):
        if not self.blocks_path and not self.occupied:
            return True
        else:
            return False

    def exit_cell(self, visitor):
        self.occupied = False

class Floor(GridCell):
    def __init__(self, color):
        super().__init__('.', color)

class Wall(GridCell):
    def __init__(self):
        super().__init__(self, '#')
        self.blocks_path = True

class Door(GridCell):
    def __init__(self, color):
        super().__init__('+', color)
        self.open = False
        if self.open == True:
            self.character = ' '
        self.locked = True
        self.broken = False

