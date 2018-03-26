import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']
sock_list = []

for i in range(100):
    sock_tuple = (random.choice(sock_types), random.choice(sock_colors))
    sock_list.append(sock_tuple)

sock_dict = {}

for j in range(len(sock_list)):
    if sock_list[j] not in sock_dict:
        sock_dict[sock_list[j]] = 1
    else:
        sock_dict[sock_list[j]] += 1

for sock in sock_dict:
    print('There are ' + str(sock_dict[sock]//2) + ' pairs, and ' + str(sock_dict[sock]%2) + ' loners of ' + sock[1] + ' ' + sock[0] + ' socks.')