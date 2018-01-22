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


def peaks_and_valleys(data):
    p = peaks(data)
    v = valleys(data)
    p_and_v = sorted(p + v)
    return p_and_v


def visual(data):
    out = ''
    for i in range(max(data), -1, -1):
        for j in range(len(data)):
            if data[j] > i:
                out = out + ' X '
            elif data[j] <= i:
                out = out + '   '
            if j == len(data) - 1:
                out = out +'\n'
    return out


n_data = [1, 2, 3, 2, 3, 4, 3, 5]
p = visual(n_data)
print(p)
print(n_data)
x = peaks(n_data)
y = valleys(n_data)
z = peaks_and_valleys(n_data)
print(x)
print(y)
print(z)