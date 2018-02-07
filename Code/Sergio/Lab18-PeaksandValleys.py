"""
Lab 18: Peaks and Valleys V1"

"""
# 7 and 9 are peaks, 4 and 6 are valleys
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):  # peak function call
    peak_index = []  #  peak index empty list
    for i in range(1, len(data)-1):  # gets list in range
        if data[i] > data[i - 1] and data[i] > data[i+1]:  # compares numbers from left to right to get peak
            peak_index.append(i)  # appends to empty list
    return peak_index


def valleys(data):  # valley function call
    valley_index = []   # valley empty list
    for i in range(1, len(data)-1):  # gets list in range
        if data[i] < data[i - 1] and data[i] < data[i+1]:  # fancy comparisons from list to get valley
            valley_index.append(i)  # appends to empty list
    return valley_index

def list():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print('peaks: '+ str(peaks(data)))
    print('valleys: ' + str(valleys(data)))


for num in data:  # visual representation of peaks and valleys
    print(' >'*num)  # prints X multiplied by num in data, looking like mountains with trees, added a space for aesthetic

print(data)
