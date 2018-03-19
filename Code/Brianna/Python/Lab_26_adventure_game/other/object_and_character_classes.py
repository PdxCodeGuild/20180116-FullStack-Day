class Character():
    """ This is a class that represents the main character in a game. """

    def __init__(self):
        """ Setting up a starting point for our character """
        self.name = "Briar"
        self.max_hit_points = 50
        self.current_hit_points = 50
        self.max_speed = 10
        self.armor_amount = 8
        self.calories = 500

    def eat(self, calories):
        self.calories += calories
        return self.calories

    def sleep(self, sleep=100):
        if sleep == 100:
            self.max_hit_points = 50
        return

    def attack(self):
        pass

class Willowisp():
    """ This sets up the methods and 'Character' that tasks are given to the player through. """
    def __init__(self):
        self.name = "Willow"
        self.location = # Random location within the area just outside of main characters home.
        self.converse = converse  # figure out how to do this.


class Enemies():
    """ This class sets up the enemies for the main character to encounter """

    def __init__(self):
        self.max_hit_points = 20
        self.current_hit_points = 20
        self.max_speed = 10
        self.armour_amount = 8

    def attack(self):
        # an if statement
        pass


class Cave_monster(Enemies):  # Common and can mainLoop around. You can see them before you run into them.
    pass


class Bandit(Enemies):  # Uncommon and you cannot see them unless you run into them. Possibly mainLoop around.
    pass


class Found_items():   # Found items can be put into a sack/inventory and used later.
    """ This class sets up the kinds of items our main character can pick up"""
    def __init__(self, name):
        self.name = name
        self.place_in_sack = True
        self.used = False



class Food():
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
        self.place_in_sack = True
        self.used = False


ham = Food('ham', 230)
casserole = Food('casserole', 100)
can_of_soup = Food('can of soup', 50)