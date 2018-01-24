# Version 1
# The way i approach it is by starting at the second number and comparing
# the data[i] value  in front and the data[i] valuer behind it. Then i just
# get i (which is not the value but the index) and store that into a new list
# and i return it.

def peaks(data):
    store_peaks = []
    for i in range(len(data)):

        if i + 2 < len(data):
            if data[i] < data[i + 1] > data[i + 2]:
                store_peaks.append(i + 1)

    return store_peaks



def valleys(data):
    store_valleys = []
    for i in range(len(data)):

        if i + 2 < len(data):
            if data[i] > data[i + 1] < data[i + 2]:
                store_valleys.append(i + 1)

    return store_valleys

# peaks and valleys combines both lists together.
def peaks_and_valleys(data):
     number_of_peaks = peaks(data)
     number_of_valleys = valleys(data)
     combined = number_of_peaks + number_of_valleys

     return combined


# only one line of code for the return combined value of
# peaks and valleys
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks_and_valleys(data))

################################################################################
# Version 2
def print_x_to_show_peaks_and_valleys(data):
    max_length = max(data)
    complete_peak_and_valley = []
    for x in range(0, max_length):
        the_x_list = []
        for i in range(len(data)):
            if data[i] >= 1:
                the_x_list.append('x')
                data[i] = data[i] - 1
            else:
                the_x_list.append(' ')
                data[i] = data[i] - 1

        complete_peak_and_valley.append(the_x_list)

    # .__len__() gives you the size of what the list is so in order to get to the actual
    # number you have to add -1 because it gives you numbers starting at 1.
    # ,-1, The second -1 is telling the computer that when it reaches -1 to stop.
    # ,-1,-1 The third -1 is because it subtract 1 each time until it reaches to negative 1.
    # This for loop wile print off each individual one in reverse.

    for i in range (complete_peak_and_valley.__len__()-1, -1, -1):
        print(' '.join(complete_peak_and_valley[i]))

new_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print_x_to_show_peaks_and_valleys(new_data)


################################################################################
# Version 3

def add_water():
    return

data_for_water = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


