"""
Lab 18: Peaks and Valleys V1"
Based off solution, but analyzed and played with the code for over an hour
"""


def peaks(data):
    peak_index = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i] # gets valley for data(7) index (6)
        right = data[i+1]
        if left < middle and right < middle:
            peak_index.append(i)
    return peak_index


def valleys(data):
    valley_index = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i] # gets valley for data(9) index(17)
        right = data[i+1]
        if left > middle and right > middle:
            valley_index.append(i)
    return valley_index

def list():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print('peaks: '+ str(peaks(data)))
    print('valleys: ' + str(valleys(data)))

list()

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

for num in data:
    print('X'*num)

print(data)
