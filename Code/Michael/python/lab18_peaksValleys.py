



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    peaks_list = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i + 1] and data[i] > data[i - 1]:
            peaks_list.append(i)
    return peaks_list


def valleys(data):
    valleys_list = []
    for i in range(1, len(data) - 1):
        if data[i] < data[i + 1] and data[i] < data[i - 1]:
            valleys_list.append(i)
    return valleys_list


print(f'Peaks {peaks(data)} and valleys {valleys(data)}')


def peaks_and_valleys(data):
    peaks_and_valleys_list = []
    peaks_and_valleys_list += peaks(data)
    peaks_and_valleys_list += valleys(data)
    return sorted(peaks_and_valleys_list)


print(f'Peaks and valleys {peaks_and_valleys(data)}')


valleys(data)
peaks(data)



