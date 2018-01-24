"""
Optional lab
Sort those socks!
"""

import random
import time
import sys

sock_types = ['ankle', 'crew', 'wool', 'knee', 'hiking']
sock_colors = ['black', 'white', 'grey', 'striped', 'checkered']
sock_list = []
new_sock_list = []
sock_dict = {}
new_sock_dict = {}

for sock in sock_types:
    sock_dict[sock] = 0

# Generate a list of 100 random socks
for i in range(0, 100):
    sock_list.append(random.choice(sock_types))

print(f"Oh no! We have a lot of disorganized socks!\n{sock_list}")
print("\nLet's sort them!")

for i in range(100):
    time.sleep(.1)
    sys.stdout.write("\rSorting elves are sorting the socks: %d%%" % i)
    sys.stdout.flush()

while len(sock_list) > 0:
    for i in range(len(sock_types)):
        sock = sock_list.pop()
        sock_dict[sock] += 1

print('\n')
for sock in sock_dict:
    print(f"You have {sock_dict[sock] // 2} pairs of {sock} socks and {sock_dict[sock] % 2} loner(s).")


