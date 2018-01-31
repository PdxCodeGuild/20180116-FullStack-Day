######finding peaks and valleys#######

def peaks(data):
    peak_indices = []
    for i in range(1,len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peak_indices.append(i)
    return peak_indices
def valleys(data):
    valley_indices = []
    for i in range[1,len(data)-1]:
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valley_indices.append(i)
    return valley_indices

def peaks_and_valleys():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(peaks(data))
    print(valleys(data))

peaks_and_valleys()
