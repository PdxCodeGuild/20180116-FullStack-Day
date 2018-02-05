import random


sock_colors = ['black', 'white', 'blue']
sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_collaction = list()


class sock:
    def __init__(self, sock_color, sock_type):
        self.color = sock_color
        self.type = sock_type



for i in range(99):
    color_random = random.randint(0, 2)
    type_random = random.randint(0, 3)
    sock_collaction.append(sock(sock_colors[color_random], sock_types[type_random]))

sock_collaction.sort(key=lambda x: (x.color, x.type))





for i in range(99):
    print("the color of the sock is " + sock_collaction[i].color + " the type is " + sock_collaction[i].type)


