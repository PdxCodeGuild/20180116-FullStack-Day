import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_list = []

for i in range(100):
    sock_list.append(random.choice(sock_types))

sock_dict = {}

for j in range(len(sock_list)):
    if sock_list[j] not in sock_dict:
        sock_dict[sock_list[j]] = 1
    else:
        sock_dict[sock_list[j]] += 1

print(sock_dict)


for sock in sock_dict:
    print('There are ' + str(sock_dict[sock]//2) + ' pairs, and ' + str(sock_dict[sock]%2) + ' loners of ' + sock + ' socks.')

