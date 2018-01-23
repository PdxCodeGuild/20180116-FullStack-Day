# Sock sorting!

# output should give the duplicates and loners for each sock type..
# example: 5: ankle, 1: crew, 7: calf ...
# to generate this, we will need to iterate through the sock list, remove an item from the list,
# to update the dictionary value, it will be sock_dict[sock_type] += 1
# to add a new key, just call the dict with the new type sock_dict[NEW] = 0

from random import choice

sock_types = ['ankle', 'crew', 'calf', 'thigh', 'slip-on']
colors = ['blue', 'black', 'argyle', 'periwinkle', 'pink']


def laundry_list():
    sock_list = []
    while len(sock_list) < 99:
        sock_list.append(choice(sock_types))
    print(sock_list)
    return sock_list


def sorted_socks(lst):
    sock_dict = {}
    for typ in sock_types:
        sock_dict[typ] = 0  # creates the keys for the dictionary
    for sock in lst:
        sock_dict[sock] += 1
    print(sock_dict)


def laundry_colors():  # make a list of tuples of socks
    sock_colors = []
    while len(sock_colors) < 99:
        rand_sock = (choice(colors), choice(sock_types))
        sock_colors.append(rand_sock)
    print(sock_colors)
    return sock_colors


def color_pairs(lst):
    sock_dict = {}
    color_types = []
    for typ in sock_types:
        for col in colors:
            color_types.append((col, typ))
    for typ in color_types:
        sock_dict[typ] = 0
    for sock in lst:
        sock_dict[sock] += 1
    print(sock_dict)
    for sock in sock_dict.keys():
        sock_dict[sock] //= 2
    print(sock_dict)

# sorted_socks(laundry_list())
color_pairs(laundry_colors())
