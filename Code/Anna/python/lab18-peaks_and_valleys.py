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
xes_list = []
rand_xes_list = []

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




