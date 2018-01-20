def valleys(data):
    valleys = []
    for i in range(1, len(data) - 1):
        if data[i - 1] > data[i] < data[i + 1]:
            valleys.append(i)
    return valleys


def peaks(data):
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i - 1] < data[i] > data[i + 1]:
            peaks.append(i)
    return peaks

data = [1, 2, 3, 2, 3, 2, 3, 2]
x = peaks(data)
y = valleys(data)
print(x)
print(y)