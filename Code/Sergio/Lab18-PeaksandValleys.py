"""
Lab 18: Peaks and Valleys V1"
Based off solution, but analyzed and played with the code for over an hour
"""
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    peak_index = []
    for i in range(1, len(data)-1):
        if data[i] > data[i - 1] and data[i] > data[i+1]:
            peak_index.append(i)
    return peak_index


def valleys(data):
    valley_index = []
    for i in range(1, len(data)-1):
        if data[i] < data[i - 1] and data[i] < data[i+1]:
            valley_index.append(i)
    return valley_index

def list():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print('peaks: '+ str(peaks(data)))
    print('valleys: ' + str(valleys(data)))

list()


for num in data:
    print('X'*num)

print(data)
