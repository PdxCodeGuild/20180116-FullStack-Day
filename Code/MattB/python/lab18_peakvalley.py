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
    for i in range(max(data), -1, -1):  #index for height of grid
        for j in range(len(data)):      #index for width of grid
            if data[j] > i:             #print out x when value of data is greater than or equal to the height
                out = out + ' X '
            elif data[j] <= i:          #print out spance when vlaue of data is smaller than the height
                out = out + '   '
            if j == len(data) - 1:      # creates new line at the index end
                out = out +'\n'
    return out


n_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
p = visual(n_data)
print(p)
print(n_data)
x = peaks(n_data)
y = valleys(n_data)
z = peaks_and_valleys(n_data)
print(f'Peaks at {x}')
print(f'Valleys at {y}')
print(f'Peaks and valleys: {z}')