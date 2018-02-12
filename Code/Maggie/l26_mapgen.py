from l26_settings import *
from l26_GridCell import *
from random import randint


class MainMap:  # the map stores levels columns, rows and cells with objects
    game_map = []
    # [map[levels[y[x]]]]
    total_levels = 10
  # the map is a list of levels and x,y cells within the level
    def __init__(self):
        MainMap.add_levels()

    @staticmethod
    def add_levels():
        for level in range(MainMap.total_levels):
            MainMap.game_map.append(MapLevel(level))

class MapLevel:  # the level is a collection of rooms
    level_contents = [] #level contains rooms with cells
    def __init__(self, level):
        self.level = level

    @staticmethod
    def fill_with_cells():
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                MapLevel.level_contents.append(GridCell())

    @staticmethod
    def generate_rooms():
        # Create a series of room instances for each level
        room_minimum_size = 5
        room_max_size = 10
        room_list = []  # lists with x,y intersects
        max_number_of_rooms = 10
        room_width = randint(room_minimum_size, room_max_size)
        room_height = randint(room_minimum_size, room_max_size)
        room_x = randint(0, BOARD_WIDTH - room_width - 1)
        room_y = randint(0, BOARD_HEIGHT - room_height - 1)

            # create a random room
        generated_room = Room(room_x, room_y, room_width, room_height)

            # does this room intersect with other rooms?
            intersects = False
            for another_room in room_list:
                if generated_room.intersect(another_room):
                    intersects = True
                    break

            if not intersects:
                room_list.append(Room())
        return room_list


class Room:  # a room is a section of the map that is filled with floor cells and joined to a tunnel by a door
    room_contents = []
    def __init__(self, x_origin, y_origin, width, height):
        self.x1 = x_origin
        self.y1 = y_origin
        self.x2 = x_origin + width
        self.y2 = y_origin + height

    def put_empty_room_in_level(self, room):  # make these tiles player passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                MapLevel.level_contents.append(Floor())

    def construct_horz_tunnel(self, x_origin, x_dest, y):
        for x in range(min(x_origin, x_dest), max(x_origin, x_dest) + 1):


    def construct_vert_tunnel(self, y_origin, y_dest, x):
        for y in range(min(y_origin, y_dest), max(y_origin, y_dest) + 1):


    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return center_x, center_y

    def intersect(self, other):
        # returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)