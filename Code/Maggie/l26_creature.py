class Creature:
    def __init__(self, y_location, x_location, character):
        self.y_location = y_location
        self.x_location = x_location
        self.character = character

    def move(self, dx, dy):
        self.x_location += dx
        self.y_location += dy


class NPC(Creature):
    def __init__(self, y_location, x_location):
        super().__init__(y_location, x_location, 'ö')

    def move(self, dx, dy):
        super().move(dx, dy)

class Player(Creature):
    def __init__(self, y_location, x_location):
        super().__init__(y_location, x_location, '@')

    def move(self, dx, dy):
        super().move(dx, dy)