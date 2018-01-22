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
