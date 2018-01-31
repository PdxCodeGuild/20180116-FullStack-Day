"""
Lab 18
Peaks and valleys
"""

import random

data_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak_list = []
valley_list = []
both_list = []
x_list = []
rand_x_list = []
new_x_list = []
xes_list = []
rand_xes_list = []
new_xes_list = []
is_x = False

rand_new_max_number = []
rand_new_x_list = []
rand_new_xes_list = []

rand_data_list = []

for i in range(0, 100):
    rand_data_list.append(random.randint(1, 9))


def peaks(data):
    # get the peaks
    for i in range(0, len(data)):
        if data[i - 1] > data[i] < data[i + 1]:
            print(f"Valley: {data[i]}")
            peak_list.append(data[i])


def valleys(data):
    # get the valleys
    for i in range(0, len(data) - 1):
        if data[i - 1] < data[i] > data[i + 1]:
            print(f"Peak: {data[i]}")
            valley_list.append(data[i])


def peaks_and_valleys():
    # return both
    both = peak_list + valley_list
    return both


peaks(data_list)
valleys(data_list)

print(f"All the peaks: {peak_list}")
print(f"All the valleys: {valley_list}")
print(f"This list has both! {peaks_and_valleys()}")


# Version 2

print("\nNow let's make it pretty!")
# make it visual

max_number = max(data_list)

for i in range(0, max_number):
    for x in range(0, len(data_list)):
        if data_list[x] >= max_number:
            x_list.append(" X ")
        else:
            x_list.append("   ")
    max_number -= 1
    xes_list.append(x_list)
    x_list = []


for l in xes_list:
    print(''.join(l))


# sideways mountain
print("")

for i in range(0, len(data_list)):
    add_x = " X " * data_list[i]
    x_list.append(add_x)
    print(add_x)

# random mountain

print("\nNow let's make a random mountain!")

rand_max_number = max(rand_data_list)

for i in range(0, rand_max_number):
    for x in range(0, len(rand_data_list)):
        if rand_data_list[x] >= rand_max_number:
            rand_x_list.append(" X ")
        else:
            rand_x_list.append("   ")
    rand_max_number -= 1
    rand_xes_list.append(rand_x_list)
    rand_x_list = []


print(rand_data_list)
print('')

for l in rand_xes_list:
    print(''.join(l))

# Version 3

print("\nLet's add some water!")

new_max_number = max(data_list)

for i in range(0, new_max_number):
    for x in range(0, len(data_list)):
        if data_list[x] >= new_max_number:
            new_x_list.append(" X ")
            is_x = True
        elif is_x:
            # loop - start from x, look ahead to see if you can find another X, found_x flag
            if new_x_list[x - 1] == " X " or new_x_list[x - 1] == " O ":    # and " X " in new_x_list[x:]
                new_x_list.append(" O ")
        else:
            new_x_list.append("   ")
    new_max_number -= 1
    new_xes_list.append(new_x_list)
    new_x_list = []
    is_x = False

for l in new_xes_list:
    print(''.join(l))


# random water mountain

print("\nRandom water!")

rand_new_max_number = max(rand_data_list)
is_x = False

for i in range(0, rand_new_max_number):
    for x in range(0, len(rand_data_list)):
        if rand_data_list[x] >= rand_new_max_number:
            rand_new_x_list.append(" X ")
            is_x = True
        elif is_x is True:
            if rand_new_x_list[x - 1] == " X " or rand_new_x_list[x - 1] == " O ":    # and " X " in new_x_list[x:]
                rand_new_x_list.append(" O ")
        else:
            rand_new_x_list.append("   ")
    rand_new_max_number -= 1
    rand_new_xes_list.append(rand_new_x_list)
    rand_new_x_list = []
    is_x = False

print(rand_data_list)
print('')

for l in rand_new_xes_list:
    print(''.join(l))
