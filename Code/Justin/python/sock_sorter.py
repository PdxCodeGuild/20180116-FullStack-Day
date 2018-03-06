import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['purple', 'blue', 'red', 'yellow']

socks = []
extra_socks = []
sock_dictionary = dict()

for i in range(100):
    socks.append((random.choice(sock_types), random.choice(sock_colors)))

print(socks)

for sock in socks:
    if sock in sock_dictionary.keys():
        sock_dictionary[sock] += 1
    else:
        sock_dictionary[sock] = 1
sock_types

print(sock_dictionary)

for sock in sock_dictionary.keys():
    if sock_dictionary[sock] % 2 == 1:
        sock_dictionary[sock] -= 1
        extra_socks.append(sock)

print(sock_dictionary)
print(extra_socks)